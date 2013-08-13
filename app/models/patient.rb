class Patient < ActiveRecord::Base
  set_table_name "patient"
  set_primary_key "patient_id"
  include Openmrs

  has_one :person, :foreign_key => :person_id, :conditions => {:voided => 0}
  has_many :patient_identifiers, :foreign_key => :patient_id, :dependent => :destroy, :conditions => {:voided => 0}
  has_many :patient_programs, :conditions => {:voided => 0}
  has_many :programs, :through => :patient_programs
  has_many :relationships, :foreign_key => :person_a, :dependent => :destroy, :conditions => {:voided => 0}
  has_many :orders, :conditions => {:voided => 0}

  has_many :program_encounters, :class_name => 'ProgramEncounter',
    :foreign_key => :patient_id, :dependent => :destroy
  
  has_many :encounters, :conditions => {:voided => 0} do 
    def find_by_date(encounter_date)
      encounter_date = Date.today unless encounter_date
      find(:all, :conditions => ["encounter_datetime BETWEEN ? AND ?", 
          encounter_date.to_date.strftime('%Y-%m-%d 00:00:00'),
          encounter_date.to_date.strftime('%Y-%m-%d 23:59:59')
        ]) # Use the SQL DATE function to compare just the date part
    end
  end

  def after_void(reason = nil)
    self.person.void(reason) rescue nil
    self.patient_identifiers.each {|row| row.void(reason) }
    self.patient_programs.each {|row| row.void(reason) }
    self.orders.each {|row| row.void(reason) }
    self.encounters.each {|row| row.void(reason) }
  end

  def name
    "#{self.person.names.first.given_name} #{self.person.names.first.family_name}"
  end
  
  def national_id
    self.patient_identifiers.find_by_identifier_type(PatientIdentifierType.find_by_name("National id").id).identifier rescue nil
  end

  def address
    "#{self.person.addresses.first.city_village}" rescue nil
  end

  def age(today = Date.today)
    return nil if self.person.birthdate.nil?

    # This code which better accounts for leap years
    patient_age = (today.year - self.person.birthdate.year) + ((today.month -
          self.person.birthdate.month) + ((today.day - self.person.birthdate.day) < 0 ? -1 : 0) < 0 ? -1 : 0)

    # If the birthdate was estimated this year, we round up the age, that way if
    # it is March and the patient says they are 25, they stay 25 (not become 24)
    birth_date=self.person.birthdate
    estimate=self.person.birthdate_estimated==1
    patient_age += (estimate && birth_date.month == 7 && birth_date.day == 1  &&
        today.month < birth_date.month && self.person.date_created.year == today.year) ? 1 : 0
  end

  def gender
    self.person.gender rescue nil
  end

  def age_in_months(today = Date.today)
    years = (today.year - self.person.birthdate.year)
    months = (today.month - self.person.birthdate.month)
    (years * 12) + months
  end

  def allergic_to_sulphur
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Allergic to sulphur").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def dpt1
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Was DPT-HepB-Hib 1 vaccine given at 6 weeks or later?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def dpt2
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Was DPT-HepB-Hib 2 vaccine given at 1 month after first dose?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def dpt3
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Was DPT-HepB-Hib 3 vaccine given at 1 month after second dose?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def pcv1
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("PCV 1 vaccine given at 6 weeks or later?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def pcv2
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("PCV 2 vaccine given at 1 month after first dose?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def pcv3
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id = ?",
          ConceptName.find_by_name("PCV 3 vaccine given at 1 month after second dose?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def bcg0
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("BCG immunization was given at birth?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def scar
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Has immunization scar been seen?").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end
  
  def polio0
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("First polio vaccine at birth").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def polio1
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Second polio vaccine at 1.5 months").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def polio2
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Third polio vaccine at 2.5 months").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def polio3
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Fourth polio vaccine at 3.5 months").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def measles9
    status = self.encounters(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :order => ["obs_datetime"], :conditions => ["concept_id = ?",
          ConceptName.find_by_name("Measles vaccine at 9 months").concept_id]).answer_string.strip rescue nil
    }.compact.flatten.last

    status = "unknown" if status.blank?
    status
  end

  def hiv_status

    @hiv_concepts = ["Previous HIV Test Status From Before Current Facility Visit", "HIV STATUS", "DNA-PCR Testing Result", "Rapid Antibody Testing Result", "Alive On ART"].collect{
      |concept| ConceptName.find_by_name(concept).concept_id rescue nil}.compact rescue []

    status = self.encounters.find(:all, :order => ["encounter_datetime ASC"]).collect { |e|
      e.observations.find(:last, :conditions => ["concept_id IN (?)",
          @hiv_concepts]).answer_string rescue nil
    }.compact.flatten.last.strip rescue ""

    status = "unknown" if status.blank?
    status = "positive" if ["reactive", "hiv infected", "positive", "+"].include?(status.downcase.strip)
    status = "negative" if ["non reactive", "non-reactive less than 3 months", "-"].include?(status.downcase.strip)
    status
  end

  def mother
    @mother_type = RelationshipType.find_by_a_is_to_b_and_b_is_to_a("Parent", "Child").relationship_type_id
    rels = Relationship.find_all_by_person_b_and_relationship(self.patient_id, @mother_type) rescue nil
    @mother = nil
    rels.each{|r|
      @mother = Patient.find(r.person_a) if Patient.find(r.person_a).gender.match(/f/i)
    }
    @mother
  end

  def is_exposed?
    status = ""

    status = "yes" if ((self.mother.hiv_status.strip == "positive") rescue false)
    concepts = ["MOTHER HIV STATUS"].collect{|name| ConceptName.find_by_name(name).concept_id rescue nil}
    status = "yes" if ((["reactive", "positive", "yes"].include?(Observation.find(:last, :order => ["obs_datetime ASC"],
            :conditions => ["person_id = ? AND concept_id IN (?)",
              self.patient_id, concepts]).answer_string.downcase.sub("-", "negative"))) rescue false)
    status
  end

  def low_birth_weight?
    status = ""
    concepts = ["BIRTH WEIGHT"].collect{|name| ConceptName.find_by_name(name).concept_id rescue nil}
    ob = Observation.find(:last, :order => ["obs_datetime ASC"],
      :conditions => ["person_id = ? AND concept_id IN (?)",
        self.patient_id, concepts]).answer_string.strip rescue nil
    status = "Yes" if ((ob.to_i > 1 && ob.to_i < 2500) rescue false)
    status
  end

  def twin_outcome?
    status = ""
    @mother_type = RelationshipType.find_by_a_is_to_b_and_b_is_to_a("Parent", "Child").relationship_type_id
    rels = Relationship.find_all_by_person_a_and_relationship(self.mother.patient_id, @mother_type) rescue nil
    rels.each{|r|
      status = "Yes" if ((((Person.find(r.person_b).birthdate - 1.months) < self.person.birthdate) ||
            ((Person.find(r.person_b).birthdate + 1.months) > self.person.birthdate)) rescue false)
    }

    status
  end

end
