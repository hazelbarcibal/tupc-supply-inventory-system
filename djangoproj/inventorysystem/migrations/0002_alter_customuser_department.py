# Generated by Django 3.2.9 on 2022-10-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorysystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(choices=[('OCS_CASHIER_SERVICES', 'OCS_CASHIER_SERVICES'), ('OES_EXTENSION_SERVICES', 'OES_EXTENSION_SERVICES'), ('OGS_GUIDANCE_SERVICES', 'OGS_GUIDANCE_SERVICES'), ('OHR_HUMAN_RESOURCES', 'OHR_HUMAN_RESOURCES'), ('OHS_HEALTH_SERVICES', 'OHS_HEALTH_SERVICES'), ('OIT_INFORMATION_TECHNOLOGY', 'OIT_INFORMATION_TECHNOLOGY'), ('OSP_JOB_PLACEMENT', 'OSP_JOB_PLACEMENT'), ('OPR_PROCUREMENT', 'OPR_PROCUREMENT'), ('ORE_RESEARCH_AND_EXTENSION', 'ORE_RESEARCH_AND_EXTENSION'), ('ORS_RESEARCH_SERVICES', 'ORS_RESEARCH_SERVICES'), ('OSA_STUDENT_AFFAIRS', 'OSA_STUDENT_AFFAIRS'), ('OSH_SECURITY_HOUSE', 'OSH_SECURITY_HOUSE'), ('DCG_DOCUMENT_CONTROL_GUIDE', 'DCG_DOCUMENT_CONTROL_GUIDE'), ('DID_INDUSTRIAL_EDUCATION', 'DID_INDUSTRIAL_EDUCATION'), ('DES_ENGINEERING_TECHNOLOGY', 'DES_ENGINEERING_TECHNOLOGY'), ('DLA_LIBERAL_ARTS', 'DLA_LIBERAL_ARTS'), ('DMS_MATH_AND_SCIENCE', 'DMS_MATH_AND_SCIENCE'), ('DPECS_PHYSICAL_EDUCATION_CULTURAL_SPORTS', 'DPECS_PHYSICAL_EDUCATION_CULTURAL_SPORTS'), ('BETEEAP_EXPANDED_TERTIARY_EDUCATION_EQUIVALENCY_AND_ACCREDITATION', 'BETEEAP_EXPANDED_TERTIARY_EDUCATION_EQUIVALENCY_AND_ACCREDITATION'), ('GAD_GENDER_AND_DEVELOPMENT', 'GAD_GENDER_AND_DEVELOPMENT'), ('IDO_INFRASTRUCTURE_DEVELOPMENT_OFFICE', 'IDO_INFRASTRUCTURE_DEVELOPMENT_OFFICE'), ('NSTP_NATIONAL_SERVICE_TRAINING_PROGRAM', 'NSTP_NATIONAL_SERVICE_TRAINING_PROGRAM'), ('OAA_ACADEMIC_AFFAIRS', 'OAA_ACADEMIC_AFFAIRS'), ('OAC_ACCOUNTING_CAMPUS', 'OAC_ACCOUNTING_CAMPUS'), ('OAD_ADMISSION', 'OAD_ADMISSION'), ('OAF_ADMIN_AND_FINANCE', 'OAF_ADMIN_AND_FINANCE'), ('OAL_ALUMNI', 'OAL_ALUMNI'), ('OAS_ADMIN_SERVICES', 'OAS_ADMIN_SERVICES'), ('OAX_AUXILIARY', 'OAX_AUXILIARY'), ('OBA_BIDS_AND_AWARDS', 'OBA_BIDS_AND_AWARDS'), ('OBD_BUDGET_DEVELOPMENT', 'OBD_BUDGET_DEVELOPMENT'), ('OCD_CAMPUS_DIRECTOR', 'OCD_CAMPUS_DIRECTOR'), ('OCL_CAMPUS_LIBRARY', 'OCL_CAMPUS_LIBRARY'), ('OCP_CAMPUS_PLANNING', 'OCP_CAMPUS_PLANNING'), ('OCR_CAMPUS_REGISTRAR', 'OCR_CAMPUS_REGISTRAR')], default='', max_length=250, verbose_name='department'),
        ),
    ]