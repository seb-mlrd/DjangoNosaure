from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib import messages
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from io import BytesIO, StringIO
from datetime import datetime
from . import models
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import base64
import csv

@admin.action(description='Exporter en PDF')
def export_pdf(modeladmin, request, queryset):
    """Export des dinosaures en PDF avec design professionnel"""
    # Créer un buffer pour le PDF
    buffer = BytesIO()
    
    # Créer le document PDF
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
    )
    
    # Créer les styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2E7D32'),
        spaceAfter=30,
        alignment=1  # center
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1B5E20'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    # Construire le contenu du PDF
    story = []
    
    # Titre principal
    story.append(Paragraph("🦖 Encyclopédie des Dinosaures", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        f"<font size=10 color='#666'>Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}</font>",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Ajouter chaque dinosaure
    queryset_list = list(queryset)
    for idx, dino in enumerate(queryset_list):
        # Titre du dinosaure
        story.append(Paragraph(f"<b>{dino.name}</b> <font size=9 color='#999'>({dino.scientific_name})</font>", heading_style))
        
        # Créer les données du tableau
        data = [
            ['Caractéristiques', ''],
            ['Taille', f"{dino.taille} m"],
            ['Poids', f"{dino.poid} kg"],
            ['Période', dino.periode.name if dino.periode else 'N/A'],
            ['Alimentation', dino.alimentation.name if dino.alimentation else 'N/A'],
        ]
        
        # Ajouter les localisations
        localisations = ', '.join([f"{l.country or ''} ({l.continent})" for l in dino.localisation.all()])
        if localisations:
            data.append(['Localisations', localisations])
        
        # Ajouter les catégories
        categories = ', '.join([c.name for c in dino.category.all()])
        if categories:
            data.append(['Catégories', categories])
        
        # Créer le tableau
        table = Table(data, colWidths=[2*inch, 4.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#C8E6C9')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1B5E20')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8F5E9')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F1F8F6')]),
        ]))
        story.append(table)
        story.append(Spacer(1, 0.3*inch))
        
        # Ajouter un saut de page entre les dinosaures (sauf le dernier)
        if idx < len(queryset_list) - 1:
            story.append(PageBreak())
    
    # Générer le PDF
    doc.build(story)
    
    # Retourner le PDF
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    
    # Déterminer le nom du fichier
    if queryset.count() == 1:
        filename = f"{queryset.first().name.replace(' ', '_')}.pdf"
    else:
        filename = f"dinosaures_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

@admin.action(description='Générer 10 dinosaures aléatoires')
def generate_random_dinosaurs(modeladmin, request, queryset):
    """Génère 10 dinosaures aléatoires"""
    try:
        output = StringIO()
        call_command('seed_dinosaurs', '--count', '10', stdout=output)
        messages.success(request, '✅ 10 dinosaures aléatoires ont été créés avec succès!')
    except Exception as e:
        messages.error(request, f'❌ Erreur lors de la génération: {str(e)}')
    
    # Rediriger vers la liste
    from django.shortcuts import redirect
    return redirect(request.path)



def export_csv(modeladmin, request, queryset):
    """Export des dinosaures en CSV avec toutes les données"""
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    
    # Déterminer le nom du fichier
    if queryset.count() == models.Dinosaur.objects.count():
        filename = f"dinosaures_complet_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    else:
        filename = f"dinosaures_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    # Créer le writer CSV avec encodage UTF-8
    writer = csv.writer(response, delimiter=';')
    
    # Écrire l'en-tête
    writer.writerow([
        'Nom', 
        'Nom scientifique', 
        'Taille (m)', 
        'Poids (kg)', 
        'Période', 
        'Alimentation',
        'Localisations',
        'Catégories',
        'Date de création'
    ])
    
    # Écrire les données
    for dino in queryset:
        # si country ou continent est present dans localisation, afficher celui-ci
        localisations = ' | '.join([f"({l.continent})" for l in dino.localisation.all()])
        categories = ' | '.join([c.name for c in dino.category.all()])
        
        writer.writerow([
            dino.name,
            dino.scientific_name,
            dino.taille,
            dino.poid,
            dino.periode.name if dino.periode else 'N/A',
            dino.alimentation.name if dino.alimentation else 'N/A',
            localisations or 'N/A',
            categories or 'N/A',
            dino.created_at.strftime('%d/%m/%Y %H:%M:%S') if dino.created_at else 'N/A'
        ])
    
    return response



class DinoAdmin(admin.ModelAdmin):
    list_display = ['name', 'taille', 'poid', 'display_photo']
    search_fields = ['name', 'scientific_name']
    list_per_page = 25
    actions = [export_pdf, export_csv, generate_random_dinosaurs]
    change_list_template = 'admin/api/dinosaur/change_list.html'
    
    def display_photo(self, obj):
        if obj.image:
            return format_html('<a href="{}"><img src="{}" style="max-height: 50px; max-width: 50px;" /></a>', obj.image.url, obj.image.url)
        return None
    
    def changelist_view(self, request, extra_context=None):
        """Surcharge pour ajouter les statistiques d'alimentation au contexte"""
        extra_context = extra_context or {}
        
        # Compter les dinosaures par type d'alimentation
        alimentation_stats = {}
        total = models.Dinosaur.objects.count()
        
        for alim in models.Alimentation.objects.all():
            count = models.Dinosaur.objects.filter(alimentation=alim).count()
            if count > 0:
                alimentation_stats[alim.name] = {
                    'count': count,
                    'percentage': round((count / total * 100), 1) if total > 0 else 0
                }
        
        # Générer le graphique
        if alimentation_stats:
            fig, ax = plt.subplots(figsize=(8, 6))
            
            labels = list(alimentation_stats.keys())
            sizes = [stat['count'] for stat in alimentation_stats.values()]
            colors_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
            
            # Créer le graphique en camembert
            pie_result = ax.pie(
                sizes, 
                labels=labels, 
                autopct='%1.1f%%',
                startangle=90,
                colors=colors_pie[:len(labels)],
                textprops={'fontsize': 12}
            )
            
            # Améliorer le style (pie_result peut avoir 2 ou 3 éléments)
            if len(pie_result) == 3:
                wedges, texts, autotexts = pie_result
                for autotext in autotexts:
                    autotext.set_color('white')
                    autotext.set_fontweight('bold')
            
            ax.set_title('Répartition des dinosaures par type d\'alimentation', 
                        fontsize=14, fontweight='bold', pad=20)
            
            # Sauvegarder dans un buffer
            buffer = BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
            plt.close(fig)
            
            # Encoder en base64
            buffer.seek(0)
            graph_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            extra_context['alimentation_graph'] = graph_base64
            extra_context['alimentation_stats'] = alimentation_stats  # type: ignore
            extra_context['total_dinosaurs'] = total  # type: ignore
        
        return super().changelist_view(request, extra_context=extra_context)
    

admin.site.register(models.Dinosaur, DinoAdmin)
admin.site.register(models.Localisation)
admin.site.register(models.Periode)
admin.site.register(models.Alimentation)
admin.site.register(models.Category)
