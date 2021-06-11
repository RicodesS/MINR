class CreateConcerts < ActiveRecord::Migration[6.0]
  def change
    create_table :concerts do |t|
      t.string :name
      t.string :id_conc
      t.string :venue

      t.timestamps
    end
  end
end
