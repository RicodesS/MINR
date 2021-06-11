class ModReports < ActiveRecord::Migration[6.0]
  def change
  	remove_column :reports, :user, :string
  	add_column :reports, :ut, :string
  end
end
