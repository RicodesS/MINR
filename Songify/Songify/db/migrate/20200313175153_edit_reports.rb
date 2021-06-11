class EditReports < ActiveRecord::Migration[6.0]
  def change
  	remove_column :reports, :comment
  	add_reference :reports, :comment
  end
end
