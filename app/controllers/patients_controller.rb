
class PatientsController < ApplicationController
  unloadable  

  before_filter :sync_user, :except => [:index, :user_login, :user_logout, 
    :set_datetime, :update_datetime, :reset_datetime]

  def show

    d = (session[:datetime].to_date rescue Date.today)
    t = Time.now
    session_date = DateTime.new(d.year, d.month, d.day, t.hour, t.min, t.sec)
   
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    if @patient.age(session_date) >= 6
      redirect_to "/encounters/age_limit" and return
    end

    
    if @patient.nil?
      redirect_to "/encounters/no_patient" and return
    end

    if params[:user_id].nil?
      redirect_to "/encounters/no_user" and return
    end

    @user = User.find(params[:user_id]) rescue nil
    
    redirect_to "/encounters/no_user" and return if @user.nil?

    @task = TaskFlow.new(params[:user_id], @patient.id, session_date.to_date)

    @links = {}

    if File.exists?("#{Rails.root}/config/protocol_task_flow.yml")
      map = YAML.load_file("#{Rails.root}/config/protocol_task_flow.yml")["#{Rails.env
        }"]["label.encounter.map"].split(",") rescue []
    end

    @label_encounter_map = {}

    map.each{ |tie|
      label = tie.split("|")[0]
      encounter = tie.split("|")[1] rescue nil

      @label_encounter_map[label] = encounter if !label.blank? && !encounter.blank?

    }

    @task_status_map = {}

    @task.tasks.each{|task|

      next if task.downcase == "update baby outcome" and (@patient.current_babies.length == 0 rescue false)
      next if !@task.current_user_activities.include?(task)

      #check if task has already been done depending on scopes
      scope = @task.task_scopes[task][:scope].upcase rescue nil
      scope = "TODAY" if scope.blank?
      encounter_name = @label_encounter_map[task.upcase]rescue nil
      concept = @task.task_scopes[task][:concept].upcase rescue nil

      @task_status_map[task] = done(scope, encounter_name, concept)
       
      ctrller = "protocol_patients"
            
      if File.exists?("#{Rails.root}/config/protocol_task_flow.yml")
        
        ctrller = YAML.load_file("#{Rails.root}/config/protocol_task_flow.yml")["#{task.downcase.gsub(/\s/, "_")}"] rescue ""
          
      end
      
      @links[task.titleize] = "/#{ctrller}/#{task.gsub(/\s/, "_")}?patient_id=#{
      @patient.id}&user_id=#{params[:user_id]}" + (task.downcase == "update baby outcome" ?
          "&baby=1&baby_total=#{(@patient.current_babies.length rescue 0)}" : "")
      
    }

    @links["Give Drugs"] = "/encounters/give_drugs?patient_id=#{@patient.id}&user_id=#{@user.id}"
 
    @project = get_global_property_value("project.name") rescue "Unknown"

    @demographics_url = get_global_property_value("patient.registration.url") rescue nil

    if !@demographics_url.nil?
      @demographics_url = @demographics_url + "/demographics/#{@patient.id}?user_id=#{@user.id}&ext=true"
    end
    @demographics_url = "http://" + @demographics_url if (!@demographics_url.match(/http:/) rescue false)
    @task.next_task

    @babies = @patient.current_babies rescue []
    
  end

  def done(scope = "", encounter_name = "", concept = "")
    scope = "" if concept.blank?
    available = []
    
    d = (session[:datetime].to_date rescue Date.today)
    t = Time.now
    session_date = DateTime.new(d.year, d.month, d.day, t.hour, t.min, t.sec)
    @task.current_date = session_date
    
    case scope
    when "TODAY"
      available = Encounter.find(:all, :joins => [:observations], :conditions =>
          ["patient_id = ? AND encounter_type = ? AND obs.concept_id = ? AND DATE(encounter_datetime) = ?",
          @task.patient.id, EncounterType.find_by_name(encounter_name).id , ConceptName.find_by_name(concept).concept_id, @task.current_date.to_date]) rescue []

    when "RECENT"
      available = Encounter.find(:all, :joins => [:observations], :conditions =>
          ["patient_id = ? AND encounter_type = ? AND obs.concept_id = ? " +
            "AND (DATE(encounter_datetime) >= ? AND DATE(encounter_datetime) <= ?)",
          @task.patient.id, EncounterType.find_by_name(encounter_name).id, ConceptName.find_by_name(concept).concept_id,
          (@task.current_date.to_date - 6.month), (@task.current_date.to_date + 6.month)]) rescue []

    when "EXISTS"
      available = Encounter.find(:all, :joins => [:observations], :conditions =>
          ["patient_id = ? AND encounter_type = ? AND obs.concept_id = ?",
          @task.patient.id, EncounterType.find_by_name(encounter_name).id, ConceptName.find_by_name(concept).concept_id]) rescue []

    when ""
      available = Encounter.find(:all, :conditions =>
          ["patient_id = ? AND encounter_type = ? AND DATE(encounter_datetime) = ?",
          @task.patient.id, EncounterType.find_by_name(encounter_name).id , @task.current_date.to_date]) rescue []
    end

    available = available.blank?? "notdone" : "done"
    available

  end

  def current_visit

    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil
    d = (session[:datetime].to_date rescue Date.today)
    t = Time.now
    session_date = DateTime.new(d.year, d.month, d.day, t.hour, t.min, t.sec)

    ProgramEncounter.current_date = session_date.to_date

    @programs = @patient.program_encounters.find(:all, :order => ["date_time DESC"],
      :conditions => ["DATE(date_time) = ?", session_date.to_date]).collect{|p|
      [
        p.id,
        p.to_s,
        p.program_encounter_types.collect{|e|
          next if e.encounter.blank?

          [
            e.encounter_id, e.encounter.type.name,
            e.encounter.encounter_datetime.strftime("%H:%M"),
            e.encounter.creator
          ]
        }.uniq.compact,
        p.date_time.strftime("%d-%b-%Y")
      ]
    } if !@patient.blank?
    
    @programs.delete_if{|prg| prg[2].blank? || (prg[2].first.blank? rescue false)}
    render :layout => false
  end

  def visit_history
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    @task = TaskFlow.new(params[:user_id], @patient.id)

    if File.exists?("#{Rails.root}/config/protocol_task_flow.yml")
      map = YAML.load_file("#{Rails.root}/config/protocol_task_flow.yml")["#{Rails.env
        }"]["label.encounter.map"].split(",") rescue []
    end

    @label_encounter_map = {}

    map.each{ |tie|
      label = tie.split("|")[0]
      encounter = tie.split("|")[1] rescue nil

      concept = @task.task_scopes[label.titleize.downcase.strip][:concept].upcase rescue ""
      key  = encounter + "|" + concept
      @label_encounter_map[key] = label if !label.blank? && !encounter.blank?
    }

    @programs = @patient.program_encounters.find(:all, :order => ["date_time DESC"]).collect{|p|

      [
        p.id,
        p.to_s,
        p.program_encounter_types.collect{|e|
          next if e.encounter.blank?
          labl = label(e.encounter_id, @label_encounter_map) || e.encounter.type.name
          [
            e.encounter_id, labl,
            e.encounter.encounter_datetime.strftime("%H:%M"),
            e.encounter.creator
          ] rescue []
        }.uniq.compact,
        p.date_time.strftime("%d-%b-%Y")
      ]
    } if !@patient.nil?

    @programs.delete_if{|prg| prg[2].blank? || (prg[2].first.blank? rescue false)}
    render :layout => false
  end

  def label(encounter_id, hash)
    concepts = Encounter.find(encounter_id).observations.collect{|ob| ob.concept.name.name.downcase}
    lbl = ""
    hash.each{|val, label|
      lbl = label if (concepts.include?(val.split("|")[1].downcase) rescue false)}
    lbl
  end
  
  def demographics
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    if @patient.nil?
      redirect_to "/encounters/no_patient" and return
    end

    if params[:user_id].nil?
      redirect_to "/encounters/no_user" and return
    end

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

      age =  0 if ConceptName.find_by_concept_id(ob.concept_id).name.match(/birth weight/i) rescue false
      age = !age.blank?? age.to_s : ((((ob.value_datetime.to_date rescue ob.obs_datetime.to_date) rescue ob.date_created.to_date) - birthdate_sec).days.to_i/(60*60*24)).to_s rescue nil
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

    birth_encounter = Observation.find_by_concept_id_and_person_id(ConceptName.find_by_name("Birth Weight").concept_id,
      @patient.id).encounter rescue nil

    Encounter.find(:all, :order => ["encounter_datetime DESC"], :conditions => ["patient_id = ?", @patient.patient_id]).collect{|enc|

      enc.encounter_datetime = @patient.person.birthdate.to_date if !birth_encounter.blank? and enc.encounter_id == birth_encounter.encounter_id
      
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
 
  protected

  def sync_user
    if !session[:user].nil?
      @user = session[:user]
    else 
      @user = JSON.parse(RestClient.get("#{@link}/verify/#{(session[:user_id])}")) rescue {}
    end
  end

end
