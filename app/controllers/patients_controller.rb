
class PatientsController < ApplicationController

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

    @task = TaskFlow.new(params[:user_id], @patient.id)

    @links = {}

    @task.tasks.each{|task|

      next if task.downcase == "update baby outcome" and (@patient.current_babies.length == 0 rescue false)

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
  
end
