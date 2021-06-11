class UpdateUsers < ActiveRecord::Migration[5.2]
    def change
      add_column :users, :username, :string, limit: 20, null: false, unique: true, default: ''
      add_column :users, :provider, :string, limit: 50, null: false, default: ''
      add_column :users, :uid, :string, limit: 500, null: false, default: ''
      add_column :users, :first_name, :string, limit: 20, null: false,  unique: true, default: ''
      add_column :users, :last_name, :string, limit: 20, null: false,  unique: true, default: ''
      add_column :users, :date_of_birth, :date, unique: true, default: ''
      add_column :users, :gender, :string, default: ''
      add_column :users, :email, :string, default: ''
      add_column :users, :twittername, :string, limit:20, null: false, unique: true, default: ''
      add_column :users, :profile_image_url, :string
      add_column :users, :location, :string
    end
end
