source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby '2.6.5'

# Gemme applicazioni esterne
gem 'rubyzip', '~> 2.0.0'

#Sweetalert
gem 'rails-assets-sweetalert2', '~> 5.1.1', source: 'https://rails-assets.org'
gem 'sweet-alert2-rails'

gem 'carrierwave', '~> 2.0'
# Use for bootstrap
gem 'bootstrap', '~> 4.3.1'
gem 'jquery-rails', '~> 4.3', '>= 4.3.3'
# Use API songkickr
gem  'songkickr'
# Use Bing maps gem
gem 'bing-location', '~> 0.0.2b'
# Use lastfm
gem 'lastfm', '>= 1.27.3'
gem 'acts_as_votable'
gem 'rake', '~> 13.0.1'
# twitter api
gem 'twitter'
# ENV Variables
gem 'dotenv-rails'
# set up devise
gem 'devise', '~> 4.2'
# Use Omniauth Twitter plugin
gem 'omniauth-twitter', '~> 1.2', '>= 1.2.1'
# Use ActiveModel has_secure_password
gem 'bcrypt-ruby', '3.1.1.rc1', :require => 'bcrypt'

# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails', '~> 5.0.0'

# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 1.3.0'


gem 'activerecord-session_store', '~> 1.0'
# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 6.0.1'
# Use sqlite3 as the database for Active Record
gem 'sqlite3', '~> 1.4'
# Use Puma as the app server
gem 'puma', '~> 4.1'
# Use SCSS for stylesheets
gem 'sass-rails', '>= 6'
# Transpile app-like JavaScript. Read more: https://github.com/rails/webpacker
gem 'webpacker', '~> 4.0'
# Turbolinks makes navigating your web application faster. Read more: https://github.com/turbolinks/turbolinks
gem 'turbolinks', '~> 5'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder', '~> 2.7'
# Use Redis adapter to run Action Cable in production
gem 'redis', '~> 4.0'

# Use Active Storage variant
# gem 'image_processing', '~> 1.2'

# Reduces boot times through caching; required in config/boot.rb
gem 'bootsnap', '>= 1.4.2', require: false

group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platforms: [:mri, :mingw, :x64_mingw]
end

group :development do
  # Access an interactive console on exception pages or by calling 'console' anywhere in the code.
  gem 'web-console', '>= 3.3.0'
  gem 'listen', '>= 3.0.5', '< 3.2'
  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'
  gem 'spring-watcher-listen', '~> 2.0.0'
end

group :test do
  # Adds support for Capybara system testing and selenium driver
  gem 'capybara', '>= 2.15'
  gem 'selenium-webdriver'
  # Easy installation and use of web drivers to run system tests with browsers
  gem 'webdrivers'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]
