
class PatientsController < ApplicationController

  before_filter :check_user

  def show
    
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    if @patient.nil?
      redirect_to "/encounters/no_patient" and return
    end

    if params[:user_id].nil?
      redirect_to "/encounters/no_user" and return
    end

    @user = User.find(params[:user_id]) rescue nil
    
    redirect_to "/encounters/no_user" and return if @user.nil?

    #check for mother hiv status

    @hiv_concepts = ["MOTHER HIV STATUS", "HIV STATUS", "DNA-PCR Testing Result", "Rapid Antibody Testing Result", "Alive On ART"].collect{|concept| ConceptName.find_by_name(concept).concept_id}.compact rescue []
    @hiv_encounters = ["IMMUNIZATION RECORD", "UPDATE HIV STATUS", "HIV STATUS AT ENROLLMENT"].collect{|enc| EncounterType.find_by_name(enc).encounter_type_id}.compact rescue []

    @is_positive = false
    
    Encounter.find(:all, :conditions => ["encounter_type IN (?)", @hiv_encounters]).collect{|enc|     
      enc }.compact.each do |enc|
      next if @is_positive == true
      @is_positive = (enc.observations.collect{|ob|
          ob.answer_string if ob.answer_string.match(/Positive|HIV Infected/i)}.compact.length > 0)

    end

    # raise @is_positive.to_yaml

    @task = TaskFlow.new(params[:user_id], @patient.id)

    @links = {}

    @task.tasks.each{|task|

      next if task.downcase == "update baby outcome" and (@patient.current_babies.length == 0 rescue false)
      next if !@task.current_user_activities.include?(task)
       
      @links[task.titleize] = "/protocol_patients/#{task.gsub(/\s/, "_")}?patient_id=#{
      @patient.id}&user_id=#{params[:user_id]}" + (task.downcase == "update baby outcome" ?
          "&baby=1&baby_total=#{(@patient.current_babies.length rescue 0)}" : "")
      
    }

    @project = get_global_property_value("project.name") rescue "Unknown"

    @demographics_url = get_global_property_value("patient.registration.url") rescue nil

    if !@demographics_url.nil?
      @demographics_url = @demographics_url + "/demographics/#{@patient.id}?user_id=#{@user.id}&ext=true"
    end
    @demographics_url = "http://" + @demographics_url if (!@demographics_url.match(/http:/) rescue false)
    @task.next_task

    @babies = @patient.current_babies rescue []
    
=begin
    @recent_encounters = []

    @programs = @patient.program_encounters.current.each{|p|

      p.program_encounter_types.each{|e|
        
        @recent_encounters << (e.encounter.type.name.downcase if p.program.name.match(/UNDER 5 PROGRAM/i) && e.encounter.encounter_datetime > 1.day.ago)
      
      } if !@patient.nil?      
    }

    @flow_destination = ""
    
    @routes = {"UNDER 5 VISIT" => "/protocol_patients/under_5_visit",
      "REASON FOR SPECIAL CARE" => "/protocol_patients/reason_for_special_care",
      "MEDICAL HISTORY" => "/protocol_patients/medical_history",
      "FAMILY MEDICAL HISTORY" => "/protocol_patients/family_medical_history",
      "IMMUNIZATION RECORD" => "/protocol_patients/immunization_record",
      "ASSESSMENT" => "/protocol_patients/assessment",
      "SUPPLIMENTATION" => "/protocol_patients/supplementation",
      "SURGICAL HISTORY" => "/protocol_patients/surgical_history",
      "INITIAL NEW BORN RECORD" => "/protocol_patients/initial_new_born_record"
    }
 
    @route_names = YAML.load_file("#{Rails.root}/config/application.yml")["#{Rails.env
        }"]["auto_flow_encounters.sequentially"].split(",") rescue []

    @route_names.each do |flow|

      next if !@flow_destination.blank?
      @flow_destination = flow if !@recent_encounters.include?(flow.downcase)
      
    end
  
    @destinationn = @routes["#{@flow_destination}"]
    unless params[:skip_flow] && params[:skip_flow].to_s == "true"
      redirect_to "#{@destinationn}/#{params[:id]}?user_id=#{params[:user_id]}&patient_id=#{params[:id]}&id=#{params[:id]}" and return if !@destinationn.blank?
    end
=end
  end

  def current_visit
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    ProgramEncounter.current_date = (session[:date_time] || Time.now)
    
    @programs = @patient.program_encounters.current.collect{|p|

      [
        p.id,
        p.to_s,
        p.program_encounter_types.collect{|e|
          [
            e.encounter_id, e.encounter.type.name,
            e.encounter.encounter_datetime.strftime("%H:%M"),
            e.encounter.creator
          ]
        },
        p.date_time.strftime("%d-%b-%Y")
      ]
    } if !@patient.nil?

    # raise @programs.inspect

    render :layout => false
  end

  def visit_history
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    @programs = @patient.program_encounters.find(:all, :order => ["date_time DESC"]).collect{|p|

      [
        p.id,
        p.to_s,
        p.program_encounter_types.collect{|e|
          [
            e.encounter_id, e.encounter.type.name,
            e.encounter.encounter_datetime.strftime("%H:%M"),
            e.encounter.creator
          ]
        },
        p.date_time.strftime("%d-%b-%Y")
      ]
    } if !@patient.nil?

    # raise @programs.inspect

    render :layout => false
  end

  def demographics
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    if @patient.nil?
      redirect_to "/encounters/no_patient" and return
    end

    if params[:user_id].nil?
      redirect_to "/encounters/no_user" and return
    end

    @user = User.find(params[:user_id]) rescue nil

    redirect_to "/encounters/no_user" and return if @user.nil?

  end

  def number_of_booked_patients
    date = params[:date].to_date
    encounter_type = EncounterType.find_by_name('Kangaroo review visit') rescue nil
    concept_id = ConceptName.find_by_name('APPOINTMENT DATE').concept_id

    count = Observation.count(:all,
      :joins => "INNER JOIN encounter e USING(encounter_id)",:group => "value_datetime",
      :conditions =>["concept_id = ? AND encounter_type = ? AND value_datetime >= ? AND value_datetime <= ?",
        concept_id,encounter_type.id,date.strftime('%Y-%m-%d 00:00:00'),date.strftime('%Y-%m-%d 23:59:59')]) rescue nil

    count = count.values unless count.blank?
    count = '0' if count.blank?

    render :text => (count.first.to_i > 0 ? {params[:date] => count}.to_json : 0)
  end

  def baby_chart

    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil
    @baby = Patient.find(params[:baby_id])

    if (@baby.gender.downcase.match(/f/i))
      file =  File.open(RAILS_ROOT + "/public/data/weight_for_age_girls.txt", "r")
    else
      file =  File.open(RAILS_ROOT + "/public/data/weight_for_age_boys.txt", "r")
    end
    @file = []
    
    file.each{ |parameters|

      line = parameters
      line = line.split(" ").join(",")
      @file << line

    }

    #get available weights

    @weights = []
    birthdate_sec = @patient.person.birthdate

    ids = ConceptName.find(:all, :conditions => ["name IN (?)", ["WEIGHT", "BIRTH WEIGHT", "BIRTH WEIGHT AT ADMISSION", "WEIGHT (KG)"]]).collect{|concept|
      concept.concept_id}
 
    Observation.find(:all, :conditions => ["person_id = ? AND concept_id IN (?)",
        @patient.id, ids]).each do |ob|
      age = ((((ob.value_datetime.to_date rescue ob.obs_datetime.to_date) rescue ob.date_created.to_date) - birthdate_sec).days.to_i/(60*60*24)).to_s rescue nil
      weight = ob.answer_string.to_i rescue nil
      next if age.blank? || weight.blank?
      weight = (weight > 100) ? weight/1000.0 : weight # quick check of weight in grams and that in KG's
      @weights << age + "," + weight.to_s if !age.blank? && !weight.blank?
    end
  end

  def chart_diagnoses
    @patient = Patient.find(params[:patient_id]) rescue (Patient.find(params[:baby_id]) rescue nil)

    age = params[:age].to_i rescue nil
    date = @patient.person.birthdate.to_date + age.months rescue nil
    result = ""
     
    Encounter.find_all_by_patient_id(@patient.patient_id).collect{|enc|
    
      if  ((enc.encounter_datetime.to_date <= date.to_date and enc.encounter_datetime.to_date >= (date - 3.months).to_date) rescue false)
        result += "</br><span style='color: white;'>" + enc.name.humanize.upcase + " (" + enc.encounter_datetime.strftime("%d-%b-%Y") + ")</br>" + "</span>"

        obs_total = 0
        enc.observations.each do |obs|
          result += "&nbsp&nbsp&nbsp" + ConceptName.find_by_concept_id(obs.concept_id).name + "&nbsp : &nbsp" + obs.answer_string + "</br>"
          obs_total += 1
        end
      end
    }

    result = "</br></br></br>&nbsp&nbsp&nbspNO DATA AVAILABLE</br></br> &nbsp&nbsp&nbspFROM  : #{(date - 3.months).strftime("%d-%b-%Y")}  (3 months back) </br> &nbsp&nbsp&nbspTO  :   #{date.strftime("%d-%b-%Y")} (Pointed)" if result.blank?
    result = "<span style='font-weight: bold;'>&nbsp&nbsp&nbsp&nbsp&nbsp&nbspAT #{age.to_s} MONTHS #{} OF AGE<br></span>" + result
    render :text => result.to_json
  end
  
end
