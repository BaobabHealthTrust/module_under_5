
class ProtocolPatientsController < ApplicationController

	def medical_history_2

	@patient = Patient.find(params[:patient_id]) rescue nil

	redirect_to '/encounters/no_patient' and return if @patient.nil?

if params[:user_id].nil?
	redirect_to '/encounters/no_user' and return
	end

	@user = User.find(params[:user_id]) rescue nil?

	redirect_to '/encounters/no_patient' and return if @user.nil?
	

	end

	def medical_history

	@patient = Patient.find(params[:patient_id]) rescue nil

	redirect_to '/encounters/no_patient' and return if @patient.nil?

if params[:user_id].nil?
	redirect_to '/encounters/no_user' and return
	end

	@user = User.find(params[:user_id]) rescue nil?

	redirect_to '/encounters/no_patient' and return if @user.nil?
	

	end

	def menu

	@patient = Patient.find(params[:patient_id]) rescue nil

	redirect_to '/encounters/no_patient' and return if @patient.nil?

if params[:user_id].nil?
	redirect_to '/encounters/no_user' and return
	end

	@user = User.find(params[:user_id]) rescue nil?

	redirect_to '/encounters/no_patient' and return if @user.nil?
	

	end

	def surgical_history

	@patient = Patient.find(params[:patient_id]) rescue nil

	redirect_to '/encounters/no_patient' and return if @patient.nil?

if params[:user_id].nil?
	redirect_to '/encounters/no_user' and return
	end

	@user = User.find(params[:user_id]) rescue nil?

	redirect_to '/encounters/no_patient' and return if @user.nil?
	

	end

end
