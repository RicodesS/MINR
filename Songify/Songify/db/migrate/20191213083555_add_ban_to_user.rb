class AddBanToUser < ActiveRecord::Migration[6.0]
  def change
    add_column :users, :ban, :boolean, default:false
  end
end
