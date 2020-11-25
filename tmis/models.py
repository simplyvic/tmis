from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User #for user model integration
from django.contrib.auth.models import User as reviewer #for user model integration
from datetime import datetime, date




################################ GENERAL MODELS TO BE CALLED IN OTHER MODELS ###############################
# class General(models.Model):
#     subnet_mask_choice = (
#             ('255.255.255.0', '255.255.255.0'),
#             ('255.255.255.240', '255.255.255.240'),
#             ('255.255.255.224', '255.255.255.224'),
#             ('255.255.255.192', '255.255.255.192'),
#         )
#     subnet_mask = models.CharField(max_length=50, default='', blank=True, null=True, choices=subnet_mask_choice)
#     os_choice = (
#             ('Windows 10', 'Windows 10'),
#             ('Windows Server 2012', 'Windows Server 2012'),
#             ('Windows Server 2008 R2', 'Windows Server 2008 R2'),
#             ('Windows 8 Home Edition', 'Windows 8 Home Edition'),
#             ('Windows 8 Professional', 'Windows 8 Professional'),
#             ('Windows 8.1 Professional', 'Windows 8.1 Professional'),
#             ('Windows 7 Ultimate', 'Windows 7 Ultimate'),
#             ('Windows 7 Professional', 'Windows 7 Professional'),
#             ('Windows 7 Home Edition', 'Windows 7 Home Edition'),
#             ('Windows XP', 'Windows XP'),
#             ('Windows Server 2003', 'Windows Server 2003'),
#             ('Mac OS X', 'Mac OS X'),
#             ('Linux', 'Linux'),
#             ('ESXi 6', 'ESXi 6'),
#             ('ESXi 5.5', 'ESXi 5.5'),
#         )
#     operating_system = models.CharField(max_length=100, default='', blank=True, null=True, choices=os_choice)
#     be_choice = (
#             ('01 Office of The President', '01 Office of The president'),
#             ('01 DLEAG Office of The President', '01 DLEAG Office of The President'),
#             ('01 Personnel Management Office', '01 Personnel Management Office'),
#             ('01 Population Secretariat', '01 Population Secretariat'),
#             ('01 Office of The Vice President', '01 Office of The Vice president'),
#             ('02 National Assembly', '02 National Assembly'),
#             ('03 Judiciary', '03 Judiciary'),
#             ('05 Public Service Commission', '05 Public service Commission'),
#             ('06 National Audit Office',  '06 National Audit Office'),
#             ('07 Army HQ', '07 Army HQ'),
#             ('07 Ministry of Defense', '07 Ministry of Defense'),
#             ('08 Gambia Police Force', '08 Gambia Police Force'),
#             ('08 Fire & Rescue Service', '08 Fire & Rescue Service'),
#             ('08 Gambia Immigration department', '08 Gambia Immigration department'),
#             ('08 Gambia Prison Service', '08 Gambia Prison Service'),
#             ('08 Ministry of Interior', '08 Ministry of Interior'),
#             ('08 Police HQ', '08 Police HQ'),
#             ('09 Ministry of Tourism and Culture', '09 Ministry of Tourism and Culture'),
#             ('10 Ministry of Foreign Affairs', '10 Ministry of Foreign Affairs'),
#             ('11 Justice', '11 Justice'),
#             ('11 Attorney General\'s Chambers & Ministry of Justice', '11 Attorney General\'s Chambers & ministry of Justice'),
#             ('12 Ministry of Finance', '12 Ministry of Finance'),
#             ('12 Accountant General Department', '12 Accountant General Department'),
#             ('12 Internal Audit', '12 Internal Audit'),
#             ('16 Ministry of local Government and Lands', '16 Ministry of local Government and Lands'),
#             ('16 Department of lands & Survey', '16 Department of lands & Survey'),
#             ('16 Department of Community Development', '16 Department of Community Development'),
#             ('16 Department Pysical Planning', '16 Department Pysical Planning'),
#             ('17 Ministry of Agriculture', '17 Ministry of Agriculture'),
#             ('17 Regional Directorate of Agriculture', '17 Regional Directorate of Agriculture'),
#             ('18 Ministry Works, Construction & Infrastructure', '18 Ministry of Works, Construction & Infrastructure'),
#             ('19 Ministry of Trade, Industry & Employment', '19 Ministry of Trade, Industry & Employment'),
#             ('20 Ministry of Basic and secondary Education', '20 Ministry of Basic and Secondary Education'),
#             ('20 MOBSE CPCU', '20 MOBSE CPCU'),
#             ('21 Ministry of Health and Social Welfare', '21 Ministry of Health and Social Welfare'),
#             ('21 Department of medical and Health', '21 Department of medical and Health'),
#             ('22 Ministry of Youth & Sports', '22 Ministry of Youth & Sports'),
#             ('23 Ministry of Environment, Climate change, Water/Resources', '23 Ministry of Environment, Climate Change,Water/Resources'),
#             ('23 Department of Water Resources', '23 Department of Water Resources'),
#             ('23 Parks and Wildlife Department', '23 Parks and Wildlife Department'),
#             ('23 Department Forestry', '23 Department Forestry'),
#             ('24 Ministry of Comm, Info & Info Tech', '24 Ministry of Comm, Info & Info Tech'),
#             ('25 Ministry of Fisheries', '25 Ministry of Fisheries'),
#             ('25 Department Fisheries', '25 Department Fisheries'),
#             ('27 Ministry Tertiary & Higher Education', '27 Ministry of Tertiary & Higher Education'),
#             ('28 Ministry of Energy', '28 Ministry of Energy'),
#             ('29 Ministry of Petroleum', '29 Ministry of petroleum'),
#             ('32 Gambia Revenue Authority', '32 Gambia Revenue Authority'),
#             ('*** OTHER DEPARTMENTS ***', '*** OTHER DEPARTMENTS ***'),
#             ('Centralized Services', 'Centralized Services'),
#             ('Independent Electoral Commission', 'Independent Electoral Commission'),
#             ('ISPEFG', 'ISPEFG'),
#             ('Alternative Dispute Resolution Secretariat', 'Alternative Dispute Resolution Secretariat'),
#             ('Gambia National Library',  'Gambia National Library'),
#             ('GamPost',  'GamPost'),
#             ('National Debt Service', 'National Debt Service'),
#             ('Ombudsman', 'Ombudsman'),
#             ('Weights & Measures Bureau', 'Weights & Measures Bureau'),
#             ('Pensions and Gratuities', 'Pensions and Gratuities'),
#             ('WARCIP Distribution ', 'WARCIP Distribution'),
#             ('*** SUB-TREASURIES ***', '*** SUB-TREASURIES ***'),
#             ('Sub-Treasury Basse', 'Sub-Treasury Basse'),
#             ('Sub-Treasury Kerewan', 'Sub-Treasury Kerewan'),
#             ('Sub-Treasury Mansakonko', 'Sub-Treasury Mansakonko'),
#             ('Sub-Treasury Janjanbureh', 'Sub-Treasury Janjanbureh'),
#             ('Sub-Treasury Brikama', 'Sub-Treasury Brikama'),
#             ('Geology Department', 'Geology Department'),
#             ('*** EMBASSIES ***', '*** EMBASSIES ***'),
#             ('Gambia Embassy Nouakchott', 'Gambia Embassy Nouakchott'),
#             ('Gambia Embassy China', 'Gambia Embassy China'),
#             ('Gambia Embassy Nigeria', 'Gambia Embassy Nigeria'),
#             ('Gambia Embassy New Delhi India', 'Gambia Embassy New Delhi India'),
#             ('Gambia Embassy France', 'Gambia Embassy France'),
#             ('Gambia Embassy Havana Cuba', 'Gambia Embassy Havana Cuba'),
#             ('Gambia Embassy Lodon UK', 'Gambia Embassy Lodon UK'),
#             ('Gambia Embassy Turkey', 'Gambia Embassy Turkey'),
#             ('Gambia Embassy Senegal,Burkina Faso,Mali', 'Gambia Embassy Senegal,Burkina Faso,Mali'),
#             ('Gambia Embassy Russia', 'Gambia Embassy Russia'),
#             ('Gambia Embassy Rabat Morocco', 'Gambia Embassy Rabat Morocco'),
#             ('Gambia Embassy Spain', 'Gambia Embassy Spain'),
#             ('Gambia Embassy South Africa', 'Gambia Embassy South Africa'),
#             ('Gambia Embassy Guinea Bissau', 'Gambia Embassy Guinea Bissau'),
#             ('Gambia Embassy Liberia', 'Gambia Embassy Liberia'),
#             ('Gambia Embassy Kuwait', 'Gambia Embassy Kuwait'),
#             ('Gambia Embassy Saudi Arabia', 'Gambia Embassy Saudi Arabia'),
#             ('****MISSIONS****', '*****MISSIONS*****'),
#             ('Permanent Mission United Nation', 'Permanent Mission United Nation'),
#             ('Permanent Mission African Union', 'Permanent Mission African Union'),
#             ('****COURTS****', '*****COURTS*****'),
#             ('Mansakonko Magistrate Court', 'Mansakonko Magistrate Court'),
#             ('Bundung Magistrate Court', 'Bundung Magistrate Court'),
#             ('Banjul Magistrate Court', 'Banjul Magistrate Court'),
#             ('Kanifing Magistrate Court', 'Kanifing Magistrate Court'),
#             ('Brikama Magistrate Court', 'Brikama Magistrate Court'),
#             ('Basse Magistrate Court', 'Basse Magistrate Court'),
#             ('Brikamaba Magistrate Court', 'Brikamaba Magistrate Court'),
#             ('Bwiam Magistrate Court', 'Bwiam Magistrate Court'),
#             ('Brikama Cadi Court', 'Brikama Cadi Court'),
#             ('Kanifing Cadi Court', 'Kanifing Cadi Court'),
#             ('Banjul Cadi Court', 'Banjul Cadi Court'),
#             ('Bansang Cadi Court', 'Bansang Cadi Court'),
#             ('Bundung Cadi Court', 'Bundung Cadi Court'),
#             ('Mansakonko Cadi Court', 'Mansakonko Cadi Court'),
#         )
#     be = models.CharField(max_length=200, default='', blank=True, null=True, choices=be_choice)
#     unit_choice = (
#             ('IT UNIT', 'IT UNIT'),
#             ('CONTROL UNIT', 'CONTROL UNIT'),
#             ('TREASURY UNIT', 'TREASURY UNIT'),
#             ('ACCOUNTING UNIT', 'ACCOUNTING UNIT'),
#             ('DATACENTER UNIT', 'DATACENTER UNIT'),
#             ('APPLICATION SUPPORT UNIT', 'APPLICATION SUPPORT UNIT'),
#             ('LOANS', 'LOANS'),
#             ('UNKNOWN', 'UNKNOWN'),
#         )
#     unit = models.CharField(max_length=50, default='', blank=True, null=True, choices=unit_choice)
#     device_class_choice = (
#             ('Computers', 'Computers'),
#             ('Servers', 'Servers'),
#             ('Routers', 'Routers'),
#             ('Switches', 'Switches'),
#             ('Printers', 'Printers'),
#             ('Basestations', 'Basestations'),
#             ('CPEs', 'CPEs'),
#         )
#     device_class = models.CharField(max_length=50, default='', blank=True, null=True, choices=device_class_choice)
#     device_type_choice = (
#             ('Desktop', 'Desktop'),
#             ('Laptop', 'Laptop'),
#             ('Application Server', 'Application Server'),
#             ('Database Server', 'Database Server'),
#             ('Domain Controller', 'Domain Controller'),
#             ('Security Server', 'Security Server'),
#             ('Monitoring Server', 'Monitoring Server'),
#             ('VMWare Host', 'VMWare Host'),
#             ('General Purpose Printer', 'General Purpose Printer'),
#             ('Cheque Printer', 'Cheque Printer'),
#             ('BreezeMAX uBasestation', 'BreezeMAX uBasestation'),
#         )
#     device_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=device_type_choice)
#     vms_host_choice = (
#             ('BJLVMS13', 'BJLVMS13'),
#             ('BJLVMS14', 'BJLVMS14'),
#             ('BJLVMS15', 'BJLVMS15'),
#             ('BJLVMS16', 'BJLVMS16'),
#             ('BJLVMS17', 'BJLVMS17'),
#             ('--------', '--------'),
#             ('KMCVMS13', 'KMCVMS13'),
#             ('KMCVMS14', 'KMCVMS14'),
#             ('KMCVMS15', 'KMCVMS15'),
#             ('KMCVMS16', 'KMCVMS16'),
#             ('Physical Server', 'Physical Server'),
#         )
#     vms_host = models.CharField(max_length=50, default='', blank=True, null=True, choices=vms_host_choice)
#     rack_number_choice = (
#             ('Rack1', 'Rack 1'),
#             ('Rack2', 'Rack 2'),
#             ('Rack3', 'Rack 3'),
#         )
#     rack_number = models.CharField(max_length=50, default='', blank=True, null=True, choices=rack_number_choice)

#     supplier_choice = (
#             ('ALLOUCH ENTERPRISE', 'ALLOUCH ENTERPRISE'),
#             ('ALVIHAG SUPERMARKET', 'ALVIHAG SUPERMARKET'),
#             ('AYOUB FURNITURE', 'AYOUB FURNITURE'),
#             ('BAYE TRADING ENTERPRISE', 'BAYE TRADING ENTERPRISE'),
#             ('BEST OPTION TRADING', 'BEST OPTION TRADING'),
#             ('CFAO MOTORS', 'CFAO MOTORS'),
#             ("DAN'S TRADING ENTERRPRISE", "DAN'S TRADING ENTERRPRISE"),
#             ('DARU HUDOS NECHANICAL', 'DARU HUDOS NECHANICAL'),
#             ('DIRNESS ENTERPRISE', 'DIRNESS ENTERPRISE'),
#             ('DOUDO THIEMDELLA THIAM AUTO', 'DOUDO THIEMDELLA THIAM AUTO'),
#             ('DRS MAN-BAI ENTERPRISE', 'DRS MAN-BAI ENTERPRISE'),
#             ('EENINBAARA AUTO CERVICES', 'EENINBAARA AUTO CERVICES'),
#             ('F.M. & S ENTERPRISE', 'F.M. & S ENTERPRISE'),
#             ('FANA FANA TRADING ENTERPRISE', 'FANA FANA TRADING ENTERPRISE'),
#             ('FI BARDAN ENTERPRISE', 'FI BARDAN ENTERPRISE'),
#             ('G 4S SECURE SOLUTIONS', 'G 4S SECURE SOLUTIONS'),
#             ('GFS BUSINESS DEVELOPMENT', 'GFS BUSINESS DEVELOPMENT'),
#             ('GORR GORR LU AUTO W/S', 'GORR GORR LU AUTO W/S'),
#             ('HG GAMBIA', 'HG GAMBIA'),
#             ('IYKE CHRIS COMPUTERS', 'IYKE CHRIS COMPUTERS'),
#             ('J MART', 'J MART'),
#             ("JABU'S TRADING", "JABU'S TRADING"),
#             ('JAWO BANNA ENTERPRISE', 'JAWO BANNA ENTERPRISE'),
#             ('JET STATIONERY LTD', 'JET STATIONERY LTD'),
#             ('JOLOF MOTOR MECHANIC WORKSHOP', 'JOLOF MOTOR MECHANIC WORKSHOP'),
#             ("KAB'S GARAGE", "KAB'S GARAGE"),
#             ('KENO AUTO PRODUCTS ENGINEERING', 'KENO AUTO PRODUCTS ENGINEERING'),
#             ('KMF TECHNOLOGIES', 'KMF TECHNOLOGIES'),
#             ('LASTING SOLUTIONS', 'LASTING SOLUTIONS'),
#             ('LIDEC TRADING ENTERPRISE', 'LIDEC TRADING ENTERPRISE'),
#             ('MODEM STATIONERY STORE', 'MODEM STATIONERY STORE'),
#             ('MP TRADING COMPANY LTD', 'MP TRADING COMPANY LTD'),
#             ('NASSER FOAM MANUFACTURING', 'NASSER FOAM MANUFACTURING'),
#             ('NIFTY ICT SOLUTION', 'NIFTY ICT SOLUTION'),
#             ('NINE 2 NINE MINI MARKET', 'NINE 2 NINE MINI MARKET'),
#             ('NJILENG TRADING', 'NJILENG TRADING'),
#             ('ONE PLUS ONE', 'ONE PLUS ONE'),
#             ('PRIME STATIONERY', 'PRIME STATIONERY'),
#             ('QUANTUM LTD', 'QUANTUM LTD'),
#             ('R&S ENTERPRISE', 'R&S ENTERPRISE'),
#             ('SHORRA STATIONERY', 'SHORRA STATIONERY'),
#             ('UNIQUE SOLUTIONS', 'UNIQUE SOLUTIONS'),
#             ('VALUE ENTERPRISE', 'VALUE ENTERPRISE'),
#         )
#     supplier_name = models.CharField(max_length=120, blank=True, null=True, choices=supplier_choice)

# ############ END GENERAL MODELS



# # class Sample(models.Model):
# #     name = models.CharField(max_length=30, blank=True, null=True)
# #     def __unicode__(self):
# #        return self.name
    
# class Unit(models.Model):
#     unit_name = models.CharField(max_length=30, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=500, blank=True, null=True)
    supervisor = models.CharField(max_length=500, blank=True, null=True)
    sdp_link = models.CharField(max_length=500, blank=True, null=True)
    lead = models.CharField(max_length=500, blank=True, null=True)
    team = models.CharField(max_length=500, blank=True, null=True)
    # unit = models.ForeignKey(Unit, max_length=500, blank=True, null=True)
    # timing = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    plan_start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    plan_due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    started = models.BooleanField(default=False)
    date_started = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    annual_plan = models.BooleanField('Annual plan activity', default=False)
    comment = models.TextField(max_length=300000, default='', blank=True, null=True)

    def __unicode__(self):
       return self.assignment_name

    def get_absolute_url(self):
       return reverse("tmis:annual_plan_edit", kwargs={"id": self.id})

    def get_absolute_url_start_activity(self):
       return reverse("tmis:start_activity", kwargs={"id": self.id})

    def get_absolute_url_end_activity(self):
       return reverse("tmis:end_activity", kwargs={"id": self.id})

# class Capacity(models.Model):
#     capacity = models.CharField('Capacity (Select the SDP capacity this will build (most relevant only!))',max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.capacity

# class Output(models.Model):
#     output = models.CharField('Output (Select the SDP output this will help deliver)', max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.output

# class Outcome(models.Model):
#     outcome = models.CharField('Outcome (Select the SDP outcome this will ultimately contribute to)', max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.outcome

class Task(models.Model):
    assignment = models.ForeignKey(Assignment, blank=True, null=True)
    task_name = models.CharField('Task', max_length=500, blank=True, null=True)
    # unit = models.ForeignKey(Unit, blank=True, null=True)
    # audit_task = models.BooleanField('This is an audit task', default=True)
    # audit_phase_choice = (
    #         ('None audit assignment', 'None audit assignment'),
    #         ('-----', '-----'),
    #         ('Pre Requisites', 'Pre Requisites'),
    #         # ('--- P1 Evaluating the Financial Reporting Framework', '--- P1 Evaluating the Financial Reporting Framework'),
    #         # ('--- P2 Review Template', '--- P2 Review Template'),
    #         # ('--- P3 Audit Query', '--- P3 Audit Query'),
    #         ('Pre Engagement', 'Pre Engagement'),
    #         # ('--- PE1 Budgeted-vs-Actual', '--- PE1 Budgeted-vs-Actual'),
    #         # ('--- PE2 Competency Matrix', '--- PE2 Competency Matrix'),
    #         # ('--- PE3 Code of ethics declaration', '--- PE3 Code of ethics declaration'),
    #         # ('--- PE4 Code of ethics conclusion', '--- PE4 Code of ethics conclusion'),
    #         # ('--- PE5 Team agreement', '--- PE5 Team agreement'),
    #         # ('--- PE6 Audit engegement letter', '--- PE6 Audit engegement letter'),
    #         # ('--- PE7 Minutes of entry meeting', '--- PE7 Minutes of entry meeting'),
    #         ('Understanding Entity', 'Understanding Entity'),
    #         ('Materiality', 'Materiality'),
    #         # ('--- 1 Pre Requisites', '--- 1 Pre Requisites'),
    #         # ('--- 2 Pre engagement', '--- 1 Pre engagement'),
    #         # ('--- 3 Understanding the entity', '--- 3 Understanding the entity'),
    #         # ('--- 4 Materiality', '--- 4 Materiality'),
    #         ('Risk Assessment', 'Risk Assessment'),
    #         # ('--- RA1 Risk assessment and response on financial statement', '--- RA1 Risk assessment and response on financial statement'),
    #         # ('--- RA2 Risk register', '--- RA2 Risk register'),
    #         # ('--- RA3 Risk response for components', '--- RA3 Risk response for components'),
    #         # ('--- RA4 Engagement team discussion document', '--- RA4 Engagement team discussion document'),
    #         # ('--- RA5 Overall audit strategy', '--- RA5 Overall audit strategy'),
    #         # ('--- RA6 QC questionnaire risk assessment', '--- RA6 QC questionnaire risk assessment'),
    #         ('Performing Audit', 'Performing Audit'),
    #         # ('--- PA1 Test of controls', '--- PA1 Test of controls'),
    #         # ('--- PA2 Lead schedule', '--- PA2 Lead schedule'),
    #         # ('--- PA3 Substantive analytical procedures', '--- PA3 Substantive analytical procedures'),
    #         # ('--- PA4 Substantive test of detail 100 testing', '--- PA4 Substantive test of detail 100 testing'),
    #         # ('--- PA5 Substantive test of detail sample testing', '--- PA5 Substantive test of detail sample testing'),
    #         # ('--- PA6 Prior current year misstatements and corrections FS Level', '--- PA6 Prior current year misstatements and corrections FS Level'),
    #         # ('--- PA7 Subsequent events FS Level', '--- PA7 Subsequent events FS Level'),
    #         ('Report', 'Report'),
    #         # ('--- R1 Management representation letter', '--- R1 Management representation letter'),
    #         # ('--- R2 Management letter', '--- R2 Management letter'),
    #         # ('--- R3 Auditors report', '--- R3 Auditors report'),
    #         # ('--- R4 Representation by audit management', '--- R4 Representation by audit management'),
    #         # ('--- R5 Matters for attention during next years audit', '--- R5 Matters for attention during next years audit'),
    #         # ('--- R6 Minutes of exit meeting', '--- R6 Minutes of exit meeting'),
    #         ('**** PERFORMANCE AUDIT ****', '**** PERFORMANCE AUDIT ****'),
    #         ('Overall Planning', 'Overall Planning'),
    #         # ('---Sector Accessment', '---Sector Accessment'),
    #         # ('---Proposal for Audit Topic', '---Proposal for Audit Topic'),
    #         # ('---Scoring of proposed Audit topics', '---Scoring of proposed Audit topics'),
    #         # ('---Priotizationg of proposed audit topic', '---Priotizationg of proposed audit topic'),
    #         ('Planning the Audit', 'Planning the Audit'),
    #         # ('---Plan for the pre-study', '---Plan for the pre-study'),
    #         # ('---Code of Ethics Declaration', '---Code of Ethics Declaration'),
    #         ('Executing the Audit', 'Executing the Audit'),
    #         ('---Engagement letter', '---Engagement letter'),
    #         ('---Minutes from meeting or interview', '---Minutes from meeting or interview'),
    #         ('---Requesting interview', '---Requesting interview'),
    #         ('Deciding and Reporting', 'Deciding and Reporting'),
    #         ('---Quality control checklist', '---Quality control checklist'),
    #         ('---Leter requesting comment on draft reports', '---Leter requesting comment on draft reports'),
    #         ('Follow up the Audit', 'Follow up the Audit'),
    #         ('---Letter on follow up on audit report', '---Letter on follow up on audit report'),
    #         ('---Follow up internal memorandum', '---Follow up internal memorandum'),
    #     )
    # audit_phase = models.CharField(max_length=500, blank=True, null=True, choices=audit_phase_choice)

    assigned_by = models.CharField(max_length=30, blank=True, null=True)
    assigned_to = models.ManyToManyField(User)
    date_assigned = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    
    completed = models.BooleanField('Task Completed', default=False)
    date_completed = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    ext = models.BooleanField('Request for time extension', default=False)
    ext_by = models.CharField('Requested by', max_length=30, blank=True, null=True)
    date_ext = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    aprv_ext = models.BooleanField('Approve time extension', default=False)
    date_apprv_ext = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    disaprv_ext = models.BooleanField('Disapprove time extension', default=False)
    date_disapprv_ext = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    sub_rev = models.BooleanField('Submit for review / Action', default=False)
    # date_sub_rev = models.BooleanField('Date submitted for review', default=False)
    review_due_date = models.DateField('Review / Action due date', auto_now_add=False, auto_now=False, blank=True, null=True)
    sub_by = models.CharField('Submitted by', max_length=30, blank=True, null=True)
    rev_level_choice = (
            ('First Level Review', 'First Level Review'),
            ('Second Level Review', 'Second Level Review'),
            ('Third Level Review', 'Third Level Review'),
            ('Completion Review', 'Completion Review'),
            ('Action', 'Action'),
        )
    rev_level = models.CharField('Level of review / Action', max_length=30, blank=True, null=True, choices=rev_level_choice)
    # reviewer = models.CharField( max_length=30, blank=True, null=True)
    reviewer = models.ForeignKey(User, blank=True, null=True, related_name='User')
    first_level_reviewer = models.CharField(max_length=30, blank=True, null=True)
    second_level_reviewer = models.CharField(max_length=30, blank=True, null=True)
    third_level_reviewer = models.CharField(max_length=30, blank=True, null=True)
    completion_reviewer = models.CharField(max_length=30, blank=True, null=True)
    action_reviewer = models.CharField(max_length=30, blank=True, null=True)
    
    date_sub_rev = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    first_level_review_rev_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    first_level_review_sent_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    second_level_review_rev_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    second_level_review_sent_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    third_level_review_rev_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    third_level_review_sent_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    completion_review_rev_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    completion_review_sent_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    action_review_rev_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    action_review_sent_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    reviewed = models.BooleanField('Reviewed / Action completed', default=False)
    date_rev = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
   
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    original_due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    working_paper = models.FileField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    add_comment = models.CharField(max_length=500, blank=True, null=True)
    conversation = models.TextField('Conversation', max_length=300000, default='', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
 
    def __unicode__(self):
       return self.task_title
   
    def get_absolute_url(self):
       return reverse("tmis:user_task_edit", kwargs={"id": self.id})

    def get_absolute_url_progress(self):
       return reverse("tmis:user_task_progress", kwargs={"id": self.id})

    def get_absolute_url_comment(self):
       return reverse("tmis:user_task_comment", kwargs={"id": self.id})

    def get_absolute_url_extension(self):
       return reverse("tmis:task_ext_edit", kwargs={"id": self.id})

    def get_absolute_url_review(self):
       return reverse("tmis:task_rev_edit", kwargs={"id": self.id})


class TaskAudit(models.Model):
    task_name = models.CharField(max_length=30, blank=True, null=True)
    # audit_phase_choice = (
    #         ('Pre Requisites', 'Pre Requisites'),
    #         ('--- P1 Evaluating the Financial Reporting Framework', '--- P1 Evaluating the Financial Reporting Framework'),
    #         ('--- P2 Review Template', '--- P2 Review Template'),
    #         ('--- P3 Audit Query', '--- P3 Audit Query'),
    #         ('Pre Engagement', 'Pre Engagement'),
    #         ('--- PE1 Budgeted-vs-Actual', '--- PE1 Budgeted-vs-Actual'),
    #         ('--- PE2 Competency Matrix', '--- PE2 Competency Matrix'),
    #         ('--- PE3 Code of ethics declaration', '--- PE3 Code of ethics declaration'),
    #         ('--- PE4 Code of ethics conclusion', '--- PE4 Code of ethics conclusion'),
    #         ('--- PE5 Team agreement', '--- PE5 Team agreement'),
    #         ('--- PE6 Audit engegement letter', '--- PE6 Audit engegement letter'),
    #         ('--- PE7 Minutes of entry meeting', '--- PE7 Minutes of entry meeting'),
    #         ('Understanding Entity', 'Understanding Entity'),
    #         ('Materiality', 'Materiality'),
    #         ('--- 1 Pre Requisites', '--- 1 Pre Requisites'),
    #         ('--- 2 Pre engagement', '--- 1 Pre engagement'),
    #         ('--- 3 Understanding the entity', '--- 3 Understanding the entity'),
    #         ('--- 4 Materiality', '--- 4 Materiality'),
    #         ('Risk Assessment', 'Risk Assessment'),
    #         ('--- RA1 Risk assessment and response on financial statement', '--- RA1 Risk assessment and response on financial statement'),
    #         ('--- RA2 Risk register', '--- RA2 Risk register'),
    #         ('--- RA3 Risk response for components', '--- RA3 Risk response for components'),
    #         ('--- RA4 Engagement team discussion document', '--- RA4 Engagement team discussion document'),
    #         ('--- RA5 Overall audit strategy', '--- RA5 Overall audit strategy'),
    #         ('--- RA6 QC questionnaire risk assessment', '--- RA6 QC questionnaire risk assessment'),
    #         ('Performing Audit', 'Performing Audit'),
    #         ('--- PA1 Test of controls', '--- PA1 Test of controls'),
    #         ('--- PA2 Lead schedule', '--- PA2 Lead schedule'),
    #         ('--- PA3 Substantive analytical procedures', '--- PA3 Substantive analytical procedures'),
    #         ('--- PA4 Substantive test of detail 100 testing', '--- PA4 Substantive test of detail 100 testing'),
    #         ('--- PA5 Substantive test of detail sample testing', '--- PA5 Substantive test of detail sample testing'),
    #         ('--- PA6 Prior current year misstatements and corrections FS Level', '--- PA6 Prior current year misstatements and corrections FS Level'),
    #         ('--- PA7 Subsequent events FS Level', '--- PA7 Subsequent events FS Level'),
    #         ('Report', 'Report'),
    #         ('--- R1 Management representation letter', '--- R1 Management representation letter'),
    #         ('--- R2 Management letter', '--- R2 Management letter'),
    #         ('--- R3 Auditors report', '--- R3 Auditors report'),
    #         ('--- R4 Representation by audit management', '--- R4 Representation by audit management'),
    #         ('--- R5 Matters for attention during next years audit', '--- R5 Matters for attention during next years audit'),
    #         ('--- R6 Minutes of exit meeting', '--- R6 Minutes of exit meeting'),
    #         ('**** PERFORMANCE AUDIT ****', '**** PERFORMANCE AUDIT ****'),
    #         ('Overall Planning', 'Overall Planning'),
    #         ('---Sector Accessment', '---Sector Accessment'),
    #         ('---Proposal for Audit Topic', '---Proposal for Audit Topic'),
    #         ('---Scoring of proposed Audit topics', '---Scoring of proposed Audit topics'),
    #         ('---Priotizationg of proposed audit topic', '---Priotizationg of proposed audit topic'),
    #         ('Planning the Audit', 'Planning the Audit'),
    #         ('---Plan for the pre-study', '---Plan for the pre-study'),
    #         ('---Code of Ethics Declaration', '---Code of Ethics Declaration'),
    #         ('Executing the Audit', 'Executing the Audit'),
    #         ('---Engagement letter', '---Engagement letter'),
    #         ('---Minutes from meeting or interview', '---Minutes from meeting or interview'),
    #         ('---Requesting interview', '---Requesting interview'),
    #         ('Deciding and Reporting', 'Deciding and Reporting'),
    #         ('---Quality control checklist', '---Quality control checklist'),
    #         ('---Leter requesting comment on draft reports', '---Leter requesting comment on draft reports'),
    #         ('Follow up the Audit', 'Follow up the Audit'),
    #         ('---Letter on follow up on audit report', '---Letter on follow up on audit report'),
    #         ('---Follow up internal memorandum', '---Follow up internal memorandum'),
    #         ('-----', '-----'),
    #         ('None audit assignment', 'None audit assignment'),
    #     )
    # audit_phase = models.CharField('Only for for audit assignment', max_length=500, blank=True, null=True, choices=audit_phase_choice)

    assigned_by = models.CharField(max_length=30, blank=True, null=True)
    assigned_to = models.OneToOneField(User)
    date_assigned = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    accept_task = models.BooleanField(default=False)
    accepted_by = models.CharField(max_length=30, blank=True, null=True)
    date_accepted = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    
    completed = models.BooleanField('Task Completed', default=False)
    date_completed = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
   
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
 
    comment = models.TextField('comments', max_length=300000, default='', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
 
    def __unicode__(self):
       return self.task_title


# class Sdp(models.Model):
#     Activity = models.ForeignKey(Assignment, blank=True, null=True)
#     task_title = models.CharField('Task', max_length=500, blank=True, null=True)
#     priority_choice = (
#             ('Critical', 'Critical'),
#             ('High', 'High'),
#             ('Medium/Low', 'Medium/Low'),
#         )
#     priority = models.CharField(max_length=30, blank=True, null=True, choices=priority_choice)#'Priority Level (keeping in mind that not everything can be critical or high!)', 
#     # Impact
#     capacity = models.ForeignKey(Capacity, blank=True, null=True)# , 
#     output = models.ForeignKey(Output, blank=True, null=True)# 
#     outcome = models.ForeignKey(Outcome, blank=True, null=True)#  
#     team_lead = models.ForeignKey(User, blank=True, null=True, related_name='Sdpteam_lead')
#     team = models.ManyToManyField(User, related_name='Sdpteam')
#     # Timing
#     start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
#     due_date = models.DateField('End date', auto_now_add=False, auto_now=False, blank=True, null=True)
    
#     resources_required = models.TextField(max_length=300000, blank=True, null=True)#'List all resources required, including estimated person days, financial costs and other assets (e.g., vehicles, meeting space and ICT)', 
#     other_notes = models.TextField(max_length=300000, blank=True, null=True)#'List all resources required, including estimated person days, financial costs and other assets (e.g., vehicles, meeting space and ICT)', 

#     completed = models.BooleanField('Task Completed', default=False)
#     date_completed = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

#     add_comment = models.CharField(max_length=500, blank=True, null=True)
#     conversation = models.TextField(max_length=300000, default='', blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
 
#     def __unicode__(self):
#        return self.task_title
   
    # def get_absolute_url(self):
    #    return reverse("tmis:user_task_edit", kwargs={"id": self.id})

    # def get_absolute_url_progress(self):
    #    return reverse("tmis:user_task_progress", kwargs={"id": self.id})

    # def get_absolute_url_comment(self):
    #    return reverse("tmis:user_task_comment", kwargs={"id": self.id})

    # def get_absolute_url_extension(self):
    #    return reverse("tmis:task_ext_edit", kwargs={"id": self.id})

    # def get_absolute_url_review(self):
    #    return reverse("tmis:task_rev_edit", kwargs={"id": self.id})






class Search(models.Model):
    assignment = models.ForeignKey(Assignment, blank=True, null=True)
    # unit = models.ForeignKey(Unit, blank=True, null=True)
    task_name = models.CharField('Task', max_length=500, blank=True, null=True)
    # audit_phase_choice = (
    #         ('Pre Requisites', 'Pre Requisites'),
    #         ('--- P1 Evaluating the Financial Reporting Framework', '--- P1 Evaluating the Financial Reporting Framework'),
    #         ('--- P2 Review Template', '--- P2 Review Template'),
    #         ('--- P3 Audit Query', '--- P3 Audit Query'),
    #         ('Pre Engagement', 'Pre Engagement'),
    #         ('--- PE1 Budgeted-vs-Actual', '--- PE1 Budgeted-vs-Actual'),
    #         ('--- PE2 Competency Matrix', '--- PE2 Competency Matrix'),
    #         ('--- PE3 Code of ethics declaration', '--- PE3 Code of ethics declaration'),
    #         ('--- PE4 Code of ethics conclusion', '--- PE4 Code of ethics conclusion'),
    #         ('--- PE5 Team agreement', '--- PE5 Team agreement'),
    #         ('--- PE6 Audit engegement letter', '--- PE6 Audit engegement letter'),
    #         ('--- PE7 Minutes of entry meeting', '--- PE7 Minutes of entry meeting'),
    #         ('Understanding Entity', 'Understanding Entity'),
    #         ('Materiality', 'Materiality'),
    #         ('--- 1 Pre Requisites', '--- 1 Pre Requisites'),
    #         ('--- 2 Pre engagement', '--- 1 Pre engagement'),
    #         ('--- 3 Understanding the entity', '--- 3 Understanding the entity'),
    #         ('--- 4 Materiality', '--- 4 Materiality'),
    #         ('Risk Assessment', 'Risk Assessment'),
    #         ('--- RA1 Risk assessment and response on financial statement', '--- RA1 Risk assessment and response on financial statement'),
    #         ('--- RA2 Risk register', '--- RA2 Risk register'),
    #         ('--- RA3 Risk response for components', '--- RA3 Risk response for components'),
    #         ('--- RA4 Engagement team discussion document', '--- RA4 Engagement team discussion documentz'),
    #         ('--- RA5 Overall audit strategy', '--- RA5 Overall audit strategy'),
    #         ('--- RA6 QC questionnaire risk assessment', '--- RA6 QC questionnaire risk assessment'),
    #         ('Performing Audit', 'Performing Audit'),
    #         ('--- PA1 Test of controls', '--- PA1 Test of controls'),
    #         ('--- PA2 Lead schedule', '--- PA2 Lead schedule'),
    #         ('--- PA3 Substantive analytical procedures', '--- PA3 Substantive analytical procedures'),
    #         ('--- PA4 Substantive test of detail 100 testing', '--- PA4 Substantive test of detail 100 testing'),
    #         ('--- PA5 Substantive test of detail sample testing', '--- PA5 Substantive test of detail sample testing'),
    #         ('--- PA6 Prior current year misstatements and corrections FS Level', '--- PA6 Prior current year misstatements and corrections FS Level'),
    #         ('--- PA7 Subsequent events FS Level', '--- PA7 Subsequent events FS Level'),
    #         ('Report', 'Report'),
    #         ('--- R1 Management representation letter', '--- R1 Management representation letter'),
    #         ('--- R2 Management letter', '--- R2 Management letter'),
    #         ('--- R3 Auditors report', '--- R3 Auditors report'),
    #         ('--- R4 Representation by audit management', '--- R4 Representation by audit management'),
    #         ('--- R5 Matters for attention during next years audit', '--- R5 Matters for attention during next years audit'),
    #         ('--- R6 Minutes of exit meeting', '--- R6 Minutes of exit meeting'),
    #         ('**** PERFORMANCE AUDIT ****', '**** PERFORMANCE AUDIT ****'),
    #         ('Overall Planning', 'Overall Planning'),
    #         ('---Sector Accessment', '---Sector Accessment'),
    #         ('---Proposal for Audit Topic', '---Proposal for Audit Topic'),
    #         ('---Scoring of proposed Audit topics', '---Scoring of proposed Audit topics'),
    #         ('---Priotizationg of proposed audit topic', '---Priotizationg of proposed audit topic'),
    #         ('Planning the Audit', 'Planning the Audit'),
    #         ('---Plan for the pre-study', '---Plan for the pre-study'),
    #         ('---Code of Ethics Declaration', '---Code of Ethics Declaration'),
    #         ('Executing the Audit', 'Executing the Audit'),
    #         ('---Engagement letter', '---Engagement letter'),
    #         ('---Minutes from meeting or interview', '---Minutes from meeting or interview'),
    #         ('---Requesting interview', '---Requesting interview'),
    #         ('Deciding and Reporting', 'Deciding and Reporting'),
    #         ('---Quality control checklist', '---Quality control checklist'),
    #         ('---Leter requesting comment on draft reports', '---Leter requesting comment on draft reports'),
    #         ('Follow up the Audit', 'Follow up the Audit'),
    #         ('---Letter on follow up on audit report', '---Letter on follow up on audit report'),
    #         ('---Follow up internal memorandum', '---Follow up internal memorandum'),
    #         ('-----', '-----'),
    #         ('None audit assignment', 'None audit assignment'),
    #     )
    # audit_phase = models.CharField(max_length=500, blank=True, null=True, choices=audit_phase_choice)
    # ext_by = models.ForeignKey(User, 'Requested by', max_length=30, blank=True, null=True, related_name='Search')
    assigned_to = models.OneToOneField(User,blank=True, null=True)
    assigned_by = models.OneToOneField(User,blank=True, null=True, related_name='UserModel')
    due_on = models.DateField('Due on or before', auto_now_add=False, auto_now=False, blank=True, null=True)



# class unit_one_head(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

# class unit_two_head(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

# class unit_three_head(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

# class unit_four_head(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

# class unit_five_head(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

# class unit_six_head(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name

# class all_unit(models.Model):
#     unit_name = models.CharField(max_length=500, blank=True, null=True)
#     def __unicode__(self):
#        return self.unit_name