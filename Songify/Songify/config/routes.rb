Rails.application.routes.draw do
  get 'valuations/update'
  post 'valuations/update'
  get 'valuations/create'
  post 'valuations/create'
  resources :concerts
  get 'favorites/update'
  post 'favorites/update'
  get 'artists/star'
  post 'artists/star'

  resources :music_events
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  root  'static_pages#homepage'

  devise_for :users , controllers: {
    session: 'users/sessions',
    registration: 'users/registrations',
    omniauth: 'users/omniauth',
    omniauth_callbacks: "users/omniauth_callbacks",
    confirmations: 'users/confirmations'}
  get 'users/index' => 'users#index', as: "users_index"
  get 'edit' => 'users#edit'
  post 'edit' => 'users#update'
  get 'sign_in' => "sessions#new" # custom path to login/sign_in
  get 'sign_up' => "registrations#new", as: "new_user_registration_path" # custom path to sign_up/registration
  # rotte _header
  get 'homepage'       => 'static_pages#homepage'  #rotta homepage
  get 'artists'        => 'artists#index'   #rotta artisti
  get 'tweet'         => 'tweet#index'    #rotta tweets
  get 'chatroom'       => 'static_pages#chatroom'  #rotta chatroom
  # rotte _footer
  get 'about'          => 'static_pages#about'     #rotta informazioni
  get 'contact'        => 'static_pages#contact'   #rotta contatti

  mount ActionCable.server => '/cable'


  resources :tweets, :concerts, :artists, :comments, :valuations, :reports
  resources :artists do
    post :rank
    patch :rank
    put :rank
    get :rank
  end
  resources :artists do
    post :star
    patch :star
    put :star
    get :star
  end
  resources :reports do
    post :create
    patch :create
    put :create
    get :create
  end
  resources :valuations do
    post :create
    patch :create
    put :create
    get :create
  end
  resources :valuations do
    post :update
    patch :update
    put :update
    get :update
  end
  resources :comments do
    member do
      put "like" => "comments#like"
    end
  end
  resources :comments do
    member do
      put "dislike" => "comments#dislike"
    end
  end
  resources :comments do
    post :create
    patch :create
    put :create
    get :create
  end
  resources :comments do
    post :update
    patch :update
    put :update
    get :update
  end
  resources :concerts do
    patch :index2
    put :index2
    get :index2
  end
  resources :concerts do
    patch :search
    put :search
    get :search
  end
  resources :concerts do
    patch :searchDate
    put :searchDate
    get :searchDate
  end
  resources :concerts do
    patch :searchZone
    put :searchZone
    get :searchZone
  end
  resources :concerts do
    patch :search_id
    put :search_id
    get :search_id
  end
   resources :users do
    patch :removeFavorite
    put :removeFavorite
    get :removeFavorite
  end
  resources :users do
    patch :addFavorite
    put :addFavorite
    get :addFavorite
  end

  resources :users do
    patch :ban
    put :ban
  end
  resources :users do
    patch :mod
    put :mod
  end
  resources :users do
    patch :admin
    put :admin
  end
  resources :users do
    patch :show_user
    put :show_user
    get :show_user
  end
  resources :users, :only =>[:show, :index, :edit, :update, :ban, :unban, :favorites]
end
