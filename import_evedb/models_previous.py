# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Agtagenttypes(models.Model):
    agenttypeid = models.IntegerField(db_column='agentTypeID', primary_key=True) # Field name made lowercase.
    agenttype = models.TextField(db_column='agentType', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agtAgentTypes'

class Agtagents(models.Model):
    agentid = models.IntegerField(db_column='agentID', primary_key=True) # Field name made lowercase.
    divisionid = models.SmallIntegerField(db_column='divisionID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True) # Field name made lowercase.
    level = models.SmallIntegerField(blank=True, null=True)
    quality = models.SmallIntegerField(blank=True, null=True)
    agenttypeid = models.IntegerField(db_column='agentTypeID', blank=True, null=True) # Field name made lowercase.
    islocator = models.NullBooleanField(db_column='isLocator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agtAgents'

class Agtresearchagents(models.Model):
    agentid = models.IntegerField(db_column='agentID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agtResearchAgents'

class Chrancestries(models.Model):
    ancestryid = models.SmallIntegerField(db_column='ancestryID', primary_key=True) # Field name made lowercase.
    ancestryname = models.CharField(db_column='ancestryName', max_length=100, blank=True) # Field name made lowercase.
    bloodlineid = models.SmallIntegerField(db_column='bloodlineID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    perception = models.SmallIntegerField(blank=True, null=True)
    willpower = models.SmallIntegerField(blank=True, null=True)
    charisma = models.SmallIntegerField(blank=True, null=True)
    memory = models.SmallIntegerField(blank=True, null=True)
    intelligence = models.SmallIntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrAncestries'

class Chrattributes(models.Model):
    attributeid = models.SmallIntegerField(db_column='attributeID', primary_key=True) # Field name made lowercase.
    attributename = models.TextField(db_column='attributeName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True) # Field name made lowercase.
    notes = models.CharField(max_length=500, blank=True)
    class Meta:
        managed = False
        db_table = 'chrAttributes'

class Chrbloodlines(models.Model):
    bloodlineid = models.SmallIntegerField(db_column='bloodlineID', primary_key=True) # Field name made lowercase.
    bloodlinename = models.CharField(db_column='bloodlineName', max_length=100, blank=True) # Field name made lowercase.
    raceid = models.SmallIntegerField(db_column='raceID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    maledescription = models.CharField(db_column='maleDescription', max_length=1000, blank=True) # Field name made lowercase.
    femaledescription = models.CharField(db_column='femaleDescription', max_length=1000, blank=True) # Field name made lowercase.
    shiptypeid = models.IntegerField(db_column='shipTypeID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    perception = models.SmallIntegerField(blank=True, null=True)
    willpower = models.SmallIntegerField(blank=True, null=True)
    charisma = models.SmallIntegerField(blank=True, null=True)
    memory = models.SmallIntegerField(blank=True, null=True)
    intelligence = models.SmallIntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True) # Field name made lowercase.
    shortmaledescription = models.CharField(db_column='shortMaleDescription', max_length=500, blank=True) # Field name made lowercase.
    shortfemaledescription = models.CharField(db_column='shortFemaleDescription', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrBloodlines'

class Chrfactions(models.Model):
    factionid = models.IntegerField(db_column='factionID', primary_key=True) # Field name made lowercase.
    factionname = models.TextField(db_column='factionName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    raceids = models.IntegerField(db_column='raceIDs', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    sizefactor = models.FloatField(db_column='sizeFactor', blank=True, null=True) # Field name made lowercase.
    stationcount = models.SmallIntegerField(db_column='stationCount', blank=True, null=True) # Field name made lowercase.
    stationsystemcount = models.SmallIntegerField(db_column='stationSystemCount', blank=True, null=True) # Field name made lowercase.
    militiacorporationid = models.IntegerField(db_column='militiaCorporationID', blank=True, null=True) # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrFactions'

class Chrraces(models.Model):
    raceid = models.SmallIntegerField(db_column='raceID', primary_key=True) # Field name made lowercase.
    racename = models.TextField(db_column='raceName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.TextField(db_column='shortDescription', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrRaces'

class Crpactivities(models.Model):
    activityid = models.SmallIntegerField(db_column='activityID', primary_key=True) # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'crpActivities'

class Crpnpccorporationdivisions(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    divisionid = models.SmallIntegerField(db_column='divisionID', primary_key=True) # Field name made lowercase.
    size = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'crpNPCCorporationDivisions'

class Crpnpccorporationresearchfields(models.Model):
    skillid = models.IntegerField(db_column='skillID', primary_key=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCCorporationResearchFields'

class Crpnpccorporationtrades(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCCorporationTrades'

class Crpnpccorporations(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    size = models.CharField(max_length=1, blank=True)
    extent = models.CharField(max_length=1, blank=True)
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    investorid1 = models.IntegerField(db_column='investorID1', blank=True, null=True) # Field name made lowercase.
    investorshares1 = models.SmallIntegerField(db_column='investorShares1', blank=True, null=True) # Field name made lowercase.
    investorid2 = models.IntegerField(db_column='investorID2', blank=True, null=True) # Field name made lowercase.
    investorshares2 = models.SmallIntegerField(db_column='investorShares2', blank=True, null=True) # Field name made lowercase.
    investorid3 = models.IntegerField(db_column='investorID3', blank=True, null=True) # Field name made lowercase.
    investorshares3 = models.SmallIntegerField(db_column='investorShares3', blank=True, null=True) # Field name made lowercase.
    investorid4 = models.IntegerField(db_column='investorID4', blank=True, null=True) # Field name made lowercase.
    investorshares4 = models.SmallIntegerField(db_column='investorShares4', blank=True, null=True) # Field name made lowercase.
    friendid = models.IntegerField(db_column='friendID', blank=True, null=True) # Field name made lowercase.
    enemyid = models.IntegerField(db_column='enemyID', blank=True, null=True) # Field name made lowercase.
    publicshares = models.BigIntegerField(db_column='publicShares', blank=True, null=True) # Field name made lowercase.
    initialprice = models.IntegerField(db_column='initialPrice', blank=True, null=True) # Field name made lowercase.
    minsecurity = models.FloatField(db_column='minSecurity', blank=True, null=True) # Field name made lowercase.
    scattered = models.NullBooleanField()
    fringe = models.SmallIntegerField(blank=True, null=True)
    corridor = models.SmallIntegerField(blank=True, null=True)
    hub = models.SmallIntegerField(blank=True, null=True)
    border = models.SmallIntegerField(blank=True, null=True)
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    sizefactor = models.FloatField(db_column='sizeFactor', blank=True, null=True) # Field name made lowercase.
    stationcount = models.SmallIntegerField(db_column='stationCount', blank=True, null=True) # Field name made lowercase.
    stationsystemcount = models.SmallIntegerField(db_column='stationSystemCount', blank=True, null=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCCorporations'

class Crpnpcdivisions(models.Model):
    divisionid = models.SmallIntegerField(db_column='divisionID', primary_key=True) # Field name made lowercase.
    divisionname = models.CharField(db_column='divisionName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    leadertype = models.CharField(db_column='leaderType', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCDivisions'

class Crtcertificates(models.Model):
    certificateid = models.IntegerField(db_column='certificateID', primary_key=True) # Field name made lowercase.
    groupid = models.SmallIntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    classid = models.IntegerField(db_column='classID', blank=True, null=True) # Field name made lowercase.
    grade = models.SmallIntegerField(blank=True, null=True)
    corpid = models.IntegerField(db_column='corpID', blank=True, null=True) # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=500, blank=True)
    class Meta:
        managed = False
        db_table = 'crtCertificates'

class Crtclasses(models.Model):
    classid = models.IntegerField(db_column='classID', primary_key=True) # Field name made lowercase.
    description = models.CharField(max_length=500, blank=True)
    classname = models.CharField(db_column='className', max_length=256, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crtClasses'

class Crtrecommendations(models.Model):
    recommendationid = models.AutoField(db_column='recommendationID', primary_key=True) # Field name made lowercase.
    shiptypeid = models.IntegerField(db_column='shipTypeID', blank=True, null=True) # Field name made lowercase.
    certificateid = models.IntegerField(db_column='certificateID', blank=True, null=True) # Field name made lowercase.
    recommendationlevel = models.SmallIntegerField(db_column='recommendationLevel') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crtRecommendations'

class Crtrelationships(models.Model):
    relationshipid = models.AutoField(db_column='relationshipID', primary_key=True) # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentID', blank=True, null=True) # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parentTypeID', blank=True, null=True) # Field name made lowercase.
    parentlevel = models.SmallIntegerField(db_column='parentLevel', blank=True, null=True) # Field name made lowercase.
    childid = models.IntegerField(db_column='childID', blank=True, null=True) # Field name made lowercase.
    grade = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'crtRelationships'

class Dgmattributecategories(models.Model):
    categoryid = models.SmallIntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=50, blank=True) # Field name made lowercase.
    categorydescription = models.CharField(db_column='categoryDescription', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmAttributeCategories'

class Dgmattributetypes(models.Model):
    attributeid = models.SmallIntegerField(db_column='attributeID', primary_key=True) # Field name made lowercase.
    attributename = models.TextField(db_column='attributeName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    defaultvalue = models.FloatField(db_column='defaultValue', blank=True, null=True) # Field name made lowercase.
    published = models.NullBooleanField()
    displayname = models.TextField(db_column='displayName', blank=True) # Field name made lowercase.
    unitid = models.SmallIntegerField(db_column='unitID', blank=True, null=True) # Field name made lowercase.
    stackable = models.NullBooleanField()
    highisgood = models.NullBooleanField(db_column='highIsGood') # Field name made lowercase.
    categoryid = models.SmallIntegerField(db_column='categoryID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmAttributeTypes'

class Dgmeffects(models.Model):
    effectid = models.SmallIntegerField(db_column='effectID', primary_key=True) # Field name made lowercase.
    effectname = models.TextField(db_column='effectName', blank=True) # Field name made lowercase.
    effectcategory = models.SmallIntegerField(db_column='effectCategory', blank=True, null=True) # Field name made lowercase.
    preexpression = models.IntegerField(db_column='preExpression', blank=True, null=True) # Field name made lowercase.
    postexpression = models.IntegerField(db_column='postExpression', blank=True, null=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    guid = models.TextField(blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    isoffensive = models.NullBooleanField(db_column='isOffensive') # Field name made lowercase.
    isassistance = models.NullBooleanField(db_column='isAssistance') # Field name made lowercase.
    durationattributeid = models.SmallIntegerField(db_column='durationAttributeID', blank=True, null=True) # Field name made lowercase.
    trackingspeedattributeid = models.SmallIntegerField(db_column='trackingSpeedAttributeID', blank=True, null=True) # Field name made lowercase.
    dischargeattributeid = models.SmallIntegerField(db_column='dischargeAttributeID', blank=True, null=True) # Field name made lowercase.
    rangeattributeid = models.SmallIntegerField(db_column='rangeAttributeID', blank=True, null=True) # Field name made lowercase.
    falloffattributeid = models.SmallIntegerField(db_column='falloffAttributeID', blank=True, null=True) # Field name made lowercase.
    disallowautorepeat = models.NullBooleanField(db_column='disallowAutoRepeat') # Field name made lowercase.
    published = models.NullBooleanField()
    displayname = models.TextField(db_column='displayName', blank=True) # Field name made lowercase.
    iswarpsafe = models.NullBooleanField(db_column='isWarpSafe') # Field name made lowercase.
    rangechance = models.NullBooleanField(db_column='rangeChance') # Field name made lowercase.
    electronicchance = models.NullBooleanField(db_column='electronicChance') # Field name made lowercase.
    propulsionchance = models.NullBooleanField(db_column='propulsionChance') # Field name made lowercase.
    distribution = models.SmallIntegerField(blank=True, null=True)
    sfxname = models.TextField(db_column='sfxName', blank=True) # Field name made lowercase.
    npcusagechanceattributeid = models.SmallIntegerField(db_column='npcUsageChanceAttributeID', blank=True, null=True) # Field name made lowercase.
    npcactivationchanceattributeid = models.SmallIntegerField(db_column='npcActivationChanceAttributeID', blank=True, null=True) # Field name made lowercase.
    fittingusagechanceattributeid = models.SmallIntegerField(db_column='fittingUsageChanceAttributeID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmEffects'

class Dgmmasteries(models.Model):
    masteryid = models.IntegerField(db_column='masteryID', primary_key=True) # Field name made lowercase.
    certificateid = models.IntegerField(db_column='certificateID') # Field name made lowercase.
    grade = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'dgmMasteries'

class Dgmtraits(models.Model):
    traitid = models.IntegerField(db_column='traitID', primary_key=True) # Field name made lowercase.
    bonustext = models.CharField(db_column='bonusText', max_length=500) # Field name made lowercase.
    unitid = models.SmallIntegerField(db_column='unitID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmTraits'

class Dgmtypeattributes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    attributeid = models.SmallIntegerField(db_column='attributeID', primary_key=True) # Field name made lowercase.
    valueint = models.IntegerField(db_column='valueInt', blank=True, null=True) # Field name made lowercase.
    valuefloat = models.FloatField(db_column='valueFloat', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmTypeAttributes'

class Dgmtypeeffects(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    effectid = models.SmallIntegerField(db_column='effectID', primary_key=True) # Field name made lowercase.
    isdefault = models.NullBooleanField(db_column='isDefault') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmTypeEffects'

class Dgmtypemasteries(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    masteryid = models.SmallIntegerField(db_column='masteryID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmTypeMasteries'

class Dgmtypetraits(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parentTypeID', primary_key=True) # Field name made lowercase.
    traitid = models.IntegerField(db_column='traitID', primary_key=True) # Field name made lowercase.
    bonus = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dgmTypeTraits'

class Evegraphics(models.Model):
    graphicid = models.IntegerField(db_column='graphicID', primary_key=True) # Field name made lowercase.
    graphicfile = models.TextField(db_column='graphicFile') # Field name made lowercase.
    description = models.TextField()
    obsolete = models.BooleanField()
    graphictype = models.TextField(db_column='graphicType', blank=True) # Field name made lowercase.
    collidable = models.NullBooleanField()
    directoryid = models.IntegerField(db_column='directoryID', blank=True, null=True) # Field name made lowercase.
    graphicname = models.CharField(db_column='graphicName', max_length=64) # Field name made lowercase.
    gfxraceid = models.TextField(db_column='gfxRaceID', blank=True) # Field name made lowercase.
    colorscheme = models.TextField(db_column='colorScheme', blank=True) # Field name made lowercase.
    sofhullname = models.TextField(db_column='sofHullName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'eveGraphics'

class Eveicons(models.Model):
    iconid = models.IntegerField(db_column='iconID', primary_key=True) # Field name made lowercase.
    iconfile = models.TextField(db_column='iconFile') # Field name made lowercase.
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'eveIcons'

class Eveunits(models.Model):
    unitid = models.SmallIntegerField(db_column='unitID', primary_key=True) # Field name made lowercase.
    unitname = models.TextField(db_column='unitName', blank=True) # Field name made lowercase.
    displayname = models.TextField(db_column='displayName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'eveUnits'

class Invblueprinttypes(models.Model):
    blueprinttypeid = models.IntegerField(db_column='blueprintTypeID', primary_key=True) # Field name made lowercase.
    parentblueprinttypeid = models.IntegerField(db_column='parentBlueprintTypeID', blank=True, null=True) # Field name made lowercase.
    producttypeid = models.IntegerField(db_column='productTypeID', blank=True, null=True) # Field name made lowercase.
    productiontime = models.IntegerField(db_column='productionTime', blank=True, null=True) # Field name made lowercase.
    techlevel = models.SmallIntegerField(db_column='techLevel', blank=True, null=True) # Field name made lowercase.
    researchproductivitytime = models.IntegerField(db_column='researchProductivityTime', blank=True, null=True) # Field name made lowercase.
    researchmaterialtime = models.IntegerField(db_column='researchMaterialTime', blank=True, null=True) # Field name made lowercase.
    researchcopytime = models.IntegerField(db_column='researchCopyTime', blank=True, null=True) # Field name made lowercase.
    researchtechtime = models.IntegerField(db_column='researchTechTime', blank=True, null=True) # Field name made lowercase.
    productivitymodifier = models.IntegerField(db_column='productivityModifier', blank=True, null=True) # Field name made lowercase.
    materialmodifier = models.SmallIntegerField(db_column='materialModifier', blank=True, null=True) # Field name made lowercase.
    wastefactor = models.SmallIntegerField(db_column='wasteFactor', blank=True, null=True) # Field name made lowercase.
    maxproductionlimit = models.IntegerField(db_column='maxProductionLimit', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invBlueprintTypes'

class Invcategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    published = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'invCategories'

class Invcontrabandtypes(models.Model):
    factionid = models.IntegerField(db_column='factionID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    standingloss = models.FloatField(db_column='standingLoss', blank=True, null=True) # Field name made lowercase.
    confiscateminsec = models.FloatField(db_column='confiscateMinSec', blank=True, null=True) # Field name made lowercase.
    finebyvalue = models.FloatField(db_column='fineByValue', blank=True, null=True) # Field name made lowercase.
    attackminsec = models.FloatField(db_column='attackMinSec', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invContrabandTypes'

class Invcontroltowerresourcepurposes(models.Model):
    purpose = models.SmallIntegerField(primary_key=True)
    purposetext = models.TextField(db_column='purposeText', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invControlTowerResourcePurposes'

class Invcontroltowerresources(models.Model):
    controltowertypeid = models.IntegerField(db_column='controlTowerTypeID', primary_key=True) # Field name made lowercase.
    resourcetypeid = models.IntegerField(db_column='resourceTypeID', primary_key=True) # Field name made lowercase.
    purpose = models.SmallIntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    minsecuritylevel = models.FloatField(db_column='minSecurityLevel', blank=True, null=True) # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invControlTowerResources'

class Invflags(models.Model):
    flagid = models.SmallIntegerField(db_column='flagID', primary_key=True) # Field name made lowercase.
    flagname = models.TextField(db_column='flagName', blank=True) # Field name made lowercase.
    flagtext = models.TextField(db_column='flagText', blank=True) # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invFlags'

class Invgroups(models.Model):
    groupid = models.IntegerField(db_column='groupID', primary_key=True) # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True) # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    usebaseprice = models.NullBooleanField(db_column='useBasePrice') # Field name made lowercase.
    allowmanufacture = models.NullBooleanField(db_column='allowManufacture') # Field name made lowercase.
    allowrecycler = models.NullBooleanField(db_column='allowRecycler') # Field name made lowercase.
    anchored = models.NullBooleanField()
    anchorable = models.NullBooleanField()
    fittablenonsingleton = models.NullBooleanField(db_column='fittableNonSingleton') # Field name made lowercase.
    published = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'invGroups'

class Invitems(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID') # Field name made lowercase.
    locationid = models.BigIntegerField(db_column='locationID') # Field name made lowercase.
    flagid = models.SmallIntegerField(db_column='flagID') # Field name made lowercase.
    quantity = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invItems'

class Invmarketgroups(models.Model):
    marketgroupid = models.IntegerField(db_column='marketGroupID', primary_key=True) # Field name made lowercase.
    parentgroupid = models.IntegerField(db_column='parentGroupID', blank=True, null=True) # Field name made lowercase.
    marketgroupname = models.CharField(db_column='marketGroupName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    hastypes = models.NullBooleanField(db_column='hasTypes') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invMarketGroups'

class Invmetagroups(models.Model):
    metagroupid = models.SmallIntegerField(db_column='metaGroupID', primary_key=True) # Field name made lowercase.
    metagroupname = models.CharField(db_column='metaGroupName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invMetaGroups'

class Invmetatypes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parentTypeID', blank=True, null=True) # Field name made lowercase.
    metagroupid = models.SmallIntegerField(db_column='metaGroupID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invMetaTypes'

class Invnames(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=200) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invNames'

class Invpositions(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    yaw = models.FloatField(blank=True, null=True)
    pitch = models.FloatField(blank=True, null=True)
    roll = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invPositions'

class Invtypematerials(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    materialtypeid = models.IntegerField(db_column='materialTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField()
    class Meta:
        #managed = False
        db_table = 'invTypeMaterials'
        unique_together = ('typeid', 'materialtypeid')

class Invtypereactions(models.Model):
    reactiontypeid = models.IntegerField(db_column='reactionTypeID', primary_key=True) # Field name made lowercase.
    input = models.BooleanField(primary_key=True)
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invTypeReactions'

class Invtypes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    mass = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    portionsize = models.IntegerField(db_column='portionSize', blank=True, null=True) # Field name made lowercase.
    raceid = models.SmallIntegerField(db_column='raceID', blank=True, null=True) # Field name made lowercase.
    baseprice = models.DecimalField(db_column='basePrice', max_digits=19, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    published = models.NullBooleanField()
    marketgroupid = models.IntegerField(db_column='marketGroupID', blank=True, null=True) # Field name made lowercase.
    chanceofduplicating = models.FloatField(db_column='chanceOfDuplicating', blank=True, null=True) # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    graphicid = models.IntegerField(db_column='graphicID', blank=True, null=True) # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    soundid = models.IntegerField(db_column='soundID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invTypes'

class Invuniquenames(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=200) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invUniqueNames'

class Mapcelestialstatistics(models.Model):
    celestialid = models.IntegerField(db_column='celestialID', primary_key=True) # Field name made lowercase.
    temperature = models.FloatField(blank=True, null=True)
    spectralclass = models.TextField(db_column='spectralClass', blank=True) # Field name made lowercase.
    luminosity = models.FloatField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    life = models.FloatField(blank=True, null=True)
    orbitradius = models.FloatField(db_column='orbitRadius', blank=True, null=True) # Field name made lowercase.
    eccentricity = models.FloatField(blank=True, null=True)
    massdust = models.FloatField(db_column='massDust', blank=True, null=True) # Field name made lowercase.
    massgas = models.FloatField(db_column='massGas', blank=True, null=True) # Field name made lowercase.
    fragmented = models.NullBooleanField()
    density = models.FloatField(blank=True, null=True)
    surfacegravity = models.FloatField(db_column='surfaceGravity', blank=True, null=True) # Field name made lowercase.
    escapevelocity = models.FloatField(db_column='escapeVelocity', blank=True, null=True) # Field name made lowercase.
    orbitperiod = models.FloatField(db_column='orbitPeriod', blank=True, null=True) # Field name made lowercase.
    rotationrate = models.FloatField(db_column='rotationRate', blank=True, null=True) # Field name made lowercase.
    locked = models.NullBooleanField()
    pressure = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mapCelestialStatistics'

class Mapconstellationjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', blank=True, null=True) # Field name made lowercase.
    fromconstellationid = models.IntegerField(db_column='fromConstellationID', primary_key=True) # Field name made lowercase.
    toconstellationid = models.IntegerField(db_column='toConstellationID', primary_key=True) # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapConstellationJumps'

class Mapconstellations(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', primary_key=True) # Field name made lowercase.
    constellationname = models.CharField(db_column='constellationName', max_length=100, blank=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True) # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True) # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True) # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True) # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True) # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True) # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mapConstellations'

class Mapdenormalize(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True) # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    orbitid = models.IntegerField(db_column='orbitID', blank=True, null=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    itemname = models.CharField(db_column='itemName', max_length=100, blank=True) # Field name made lowercase.
    security = models.FloatField(blank=True, null=True)
    celestialindex = models.SmallIntegerField(db_column='celestialIndex', blank=True, null=True) # Field name made lowercase.
    orbitindex = models.SmallIntegerField(db_column='orbitIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapDenormalize'

class Mapjumps(models.Model):
    stargateid = models.IntegerField(db_column='stargateID', primary_key=True) # Field name made lowercase.
    celestialid = models.IntegerField(db_column='celestialID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapJumps'

class Maplandmarks(models.Model):
    landmarkid = models.SmallIntegerField(db_column='landmarkID', primary_key=True) # Field name made lowercase.
    landmarkname = models.TextField(db_column='landmarkName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    importance = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mapLandmarks'

class Maplocationscenes(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True) # Field name made lowercase.
    graphicid = models.IntegerField(db_column='graphicID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapLocationScenes'

class Maplocationwormholeclasses(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True) # Field name made lowercase.
    wormholeclassid = models.SmallIntegerField(db_column='wormholeClassID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapLocationWormholeClasses'

class Mapregionjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', primary_key=True) # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapRegionJumps'

class Mapregions(models.Model):
    regionid = models.IntegerField(db_column='regionID', primary_key=True) # Field name made lowercase.
    regionname = models.CharField(db_column='regionName', max_length=100, blank=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True) # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True) # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True) # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True) # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True) # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True) # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mapRegions'

class Mapsolarsystemjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', blank=True, null=True) # Field name made lowercase.
    fromconstellationid = models.IntegerField(db_column='fromConstellationID', blank=True, null=True) # Field name made lowercase.
    fromsolarsystemid = models.IntegerField(db_column='fromSolarSystemID', primary_key=True) # Field name made lowercase.
    tosolarsystemid = models.IntegerField(db_column='toSolarSystemID', primary_key=True) # Field name made lowercase.
    toconstellationid = models.IntegerField(db_column='toConstellationID', blank=True, null=True) # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapSolarSystemJumps'

class Mapsolarsystems(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', primary_key=True) # Field name made lowercase.
    solarsystemname = models.CharField(db_column='solarSystemName', max_length=100, blank=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True) # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True) # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True) # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True) # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True) # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True) # Field name made lowercase.
    luminosity = models.FloatField(blank=True, null=True)
    border = models.NullBooleanField()
    fringe = models.NullBooleanField()
    corridor = models.NullBooleanField()
    hub = models.NullBooleanField()
    international = models.NullBooleanField()
    regional = models.NullBooleanField()
    constellation = models.NullBooleanField()
    security = models.FloatField(blank=True, null=True)
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    suntypeid = models.IntegerField(db_column='sunTypeID', blank=True, null=True) # Field name made lowercase.
    securityclass = models.TextField(db_column='securityClass', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapSolarSystems'

class Mapuniverse(models.Model):
    universeid = models.IntegerField(db_column='universeID', primary_key=True) # Field name made lowercase.
    universename = models.TextField(db_column='universeName', blank=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True) # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True) # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True) # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True) # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True) # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True) # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mapUniverse'

class Planetschematics(models.Model):
    schematicid = models.SmallIntegerField(db_column='schematicID', primary_key=True) # Field name made lowercase.
    schematicname = models.CharField(db_column='schematicName', max_length=255, blank=True) # Field name made lowercase.
    cycletime = models.IntegerField(db_column='cycleTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'planetSchematics'

class Planetschematicspinmap(models.Model):
    schematicid = models.SmallIntegerField(db_column='schematicID', primary_key=True) # Field name made lowercase.
    pintypeid = models.IntegerField(db_column='pinTypeID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'planetSchematicsPinMap'

class Planetschematicstypemap(models.Model):
    schematicid = models.SmallIntegerField(db_column='schematicID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    isinput = models.NullBooleanField(db_column='isInput') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'planetSchematicsTypeMap'

class Ramactivities(models.Model):
    activityid = models.SmallIntegerField(db_column='activityID', primary_key=True) # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=100, blank=True) # Field name made lowercase.
    iconno = models.TextField(db_column='iconNo', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    published = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ramActivities'

class Ramassemblylinestations(models.Model):
    stationid = models.IntegerField(db_column='stationID', primary_key=True) # Field name made lowercase.
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True) # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineStations'

class Ramassemblylinetypedetailpercategory(models.Model):
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    timemultiplier = models.FloatField(db_column='timeMultiplier', blank=True, null=True) # Field name made lowercase.
    materialmultiplier = models.FloatField(db_column='materialMultiplier', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerCategory'

class Ramassemblylinetypedetailpergroup(models.Model):
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', primary_key=True) # Field name made lowercase.
    timemultiplier = models.FloatField(db_column='timeMultiplier', blank=True, null=True) # Field name made lowercase.
    materialmultiplier = models.FloatField(db_column='materialMultiplier', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerGroup'

class Ramassemblylinetypes(models.Model):
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    assemblylinetypename = models.CharField(db_column='assemblyLineTypeName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    basetimemultiplier = models.FloatField(db_column='baseTimeMultiplier', blank=True, null=True) # Field name made lowercase.
    basematerialmultiplier = models.FloatField(db_column='baseMaterialMultiplier', blank=True, null=True) # Field name made lowercase.
    volume = models.FloatField(blank=True, null=True)
    activityid = models.SmallIntegerField(db_column='activityID', blank=True, null=True) # Field name made lowercase.
    mincostperhour = models.FloatField(db_column='minCostPerHour', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypes'

class Ramassemblylines(models.Model):
    assemblylineid = models.IntegerField(db_column='assemblyLineID', primary_key=True) # Field name made lowercase.
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', blank=True, null=True) # Field name made lowercase.
    containerid = models.IntegerField(db_column='containerID', blank=True, null=True) # Field name made lowercase.
    nextfreetime = models.DateTimeField(db_column='nextFreeTime', blank=True, null=True) # Field name made lowercase.
    uigroupingid = models.SmallIntegerField(db_column='UIGroupingID', blank=True, null=True) # Field name made lowercase.
    costinstall = models.FloatField(db_column='costInstall', blank=True, null=True) # Field name made lowercase.
    costperhour = models.FloatField(db_column='costPerHour', blank=True, null=True) # Field name made lowercase.
    restrictionmask = models.SmallIntegerField(db_column='restrictionMask', blank=True, null=True) # Field name made lowercase.
    discountpergoodstandingpoint = models.FloatField(db_column='discountPerGoodStandingPoint', blank=True, null=True) # Field name made lowercase.
    surchargeperbadstandingpoint = models.FloatField(db_column='surchargePerBadStandingPoint', blank=True, null=True) # Field name made lowercase.
    minimumstanding = models.FloatField(db_column='minimumStanding', blank=True, null=True) # Field name made lowercase.
    minimumcharsecurity = models.FloatField(db_column='minimumCharSecurity', blank=True, null=True) # Field name made lowercase.
    minimumcorpsecurity = models.FloatField(db_column='minimumCorpSecurity', blank=True, null=True) # Field name made lowercase.
    maximumcharsecurity = models.FloatField(db_column='maximumCharSecurity', blank=True, null=True) # Field name made lowercase.
    maximumcorpsecurity = models.FloatField(db_column='maximumCorpSecurity', blank=True, null=True) # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID', blank=True, null=True) # Field name made lowercase.
    activityid = models.SmallIntegerField(db_column='activityID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLines'

class Raminstallationtypecontents(models.Model):
    installationtypeid = models.IntegerField(db_column='installationTypeID', primary_key=True) # Field name made lowercase.
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ramInstallationTypeContents'

class Ramtyperequirements(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    activityid = models.SmallIntegerField(db_column='activityID', primary_key=True) # Field name made lowercase.
    requiredtypeid = models.IntegerField(db_column='requiredTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    damageperjob = models.FloatField(db_column='damagePerJob', blank=True, null=True) # Field name made lowercase.
    recycle = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ramTypeRequirements'

class Staoperationservices(models.Model):
    operationid = models.SmallIntegerField(db_column='operationID', primary_key=True) # Field name made lowercase.
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'staOperationServices'

class Staoperations(models.Model):
    activityid = models.SmallIntegerField(db_column='activityID', blank=True, null=True) # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationID', primary_key=True) # Field name made lowercase.
    operationname = models.CharField(db_column='operationName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    fringe = models.SmallIntegerField(blank=True, null=True)
    corridor = models.SmallIntegerField(blank=True, null=True)
    hub = models.SmallIntegerField(blank=True, null=True)
    border = models.SmallIntegerField(blank=True, null=True)
    ratio = models.SmallIntegerField(blank=True, null=True)
    caldaristationtypeid = models.IntegerField(db_column='caldariStationTypeID', blank=True, null=True) # Field name made lowercase.
    minmatarstationtypeid = models.IntegerField(db_column='minmatarStationTypeID', blank=True, null=True) # Field name made lowercase.
    amarrstationtypeid = models.IntegerField(db_column='amarrStationTypeID', blank=True, null=True) # Field name made lowercase.
    gallentestationtypeid = models.IntegerField(db_column='gallenteStationTypeID', blank=True, null=True) # Field name made lowercase.
    jovestationtypeid = models.IntegerField(db_column='joveStationTypeID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'staOperations'

class Staservices(models.Model):
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True) # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'staServices'

class Stastationtypes(models.Model):
    stationtypeid = models.IntegerField(db_column='stationTypeID', primary_key=True) # Field name made lowercase.
    dockentryx = models.FloatField(db_column='dockEntryX', blank=True, null=True) # Field name made lowercase.
    dockentryy = models.FloatField(db_column='dockEntryY', blank=True, null=True) # Field name made lowercase.
    dockentryz = models.FloatField(db_column='dockEntryZ', blank=True, null=True) # Field name made lowercase.
    dockorientationx = models.FloatField(db_column='dockOrientationX', blank=True, null=True) # Field name made lowercase.
    dockorientationy = models.FloatField(db_column='dockOrientationY', blank=True, null=True) # Field name made lowercase.
    dockorientationz = models.FloatField(db_column='dockOrientationZ', blank=True, null=True) # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationID', blank=True, null=True) # Field name made lowercase.
    officeslots = models.SmallIntegerField(db_column='officeSlots', blank=True, null=True) # Field name made lowercase.
    reprocessingefficiency = models.FloatField(db_column='reprocessingEfficiency', blank=True, null=True) # Field name made lowercase.
    conquerable = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'staStationTypes'

class Stastations(models.Model):
    stationid = models.IntegerField(db_column='stationID', primary_key=True) # Field name made lowercase.
    security = models.SmallIntegerField(blank=True, null=True)
    dockingcostpervolume = models.FloatField(db_column='dockingCostPerVolume', blank=True, null=True) # Field name made lowercase.
    maxshipvolumedockable = models.FloatField(db_column='maxShipVolumeDockable', blank=True, null=True) # Field name made lowercase.
    officerentalcost = models.IntegerField(db_column='officeRentalCost', blank=True, null=True) # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationID', blank=True, null=True) # Field name made lowercase.
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True) # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    stationname = models.CharField(db_column='stationName', max_length=100, blank=True) # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    reprocessingefficiency = models.FloatField(db_column='reprocessingEfficiency', blank=True, null=True) # Field name made lowercase.
    reprocessingstationstake = models.FloatField(db_column='reprocessingStationsTake', blank=True, null=True) # Field name made lowercase.
    reprocessinghangarflag = models.SmallIntegerField(db_column='reprocessingHangarFlag', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'staStations'

class Translationtables(models.Model):
    sourcetable = models.CharField(db_column='sourceTable', primary_key=True, max_length=200) # Field name made lowercase.
    destinationtable = models.CharField(db_column='destinationTable', max_length=200, blank=True) # Field name made lowercase.
    translatedkey = models.CharField(db_column='translatedKey', primary_key=True, max_length=200) # Field name made lowercase.
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True) # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'translationTables'

class Trntranslationcolumns(models.Model):
    tcgroupid = models.SmallIntegerField(db_column='tcGroupID', blank=True, null=True) # Field name made lowercase.
    tcid = models.SmallIntegerField(db_column='tcID', primary_key=True) # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=256) # Field name made lowercase.
    columnname = models.CharField(db_column='columnName', max_length=128) # Field name made lowercase.
    masterid = models.CharField(db_column='masterID', max_length=128, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'trnTranslationColumns'

class Trntranslationlanguages(models.Model):
    numericlanguageid = models.IntegerField(db_column='numericLanguageID', primary_key=True) # Field name made lowercase.
    languageid = models.TextField(db_column='languageID', blank=True) # Field name made lowercase.
    languagename = models.CharField(db_column='languageName', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'trnTranslationLanguages'

class Trntranslations(models.Model):
    tcid = models.SmallIntegerField(db_column='tcID', primary_key=True) # Field name made lowercase.
    keyid = models.IntegerField(db_column='keyID', primary_key=True) # Field name made lowercase.
    languageid = models.TextField(db_column='languageID', primary_key=True) # Field name made lowercase.
    text = models.TextField()
    class Meta:
        managed = False
        db_table = 'trnTranslations'

class Warcombatzonesystems(models.Model):
    solarsystemid = models.IntegerField(db_column='solarSystemID', primary_key=True) # Field name made lowercase.
    combatzoneid = models.IntegerField(db_column='combatZoneID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'warCombatZoneSystems'

class Warcombatzones(models.Model):
    combatzoneid = models.IntegerField(db_column='combatZoneID', primary_key=True) # Field name made lowercase.
    combatzonename = models.CharField(db_column='combatZoneName', max_length=100, blank=True) # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    centersystemid = models.IntegerField(db_column='centerSystemID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=500, blank=True)
    class Meta:
        managed = False
        db_table = 'warCombatZones'

