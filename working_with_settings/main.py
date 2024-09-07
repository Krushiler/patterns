from working_with_settings.di.di import Di

di_container = Di()

sm1 = di_container.get_settings_manager()

# Windows absolute path expample
# C:\\Users\\User\\Downloads\\settings_success.json
sm1.open('assets/settings_success.json')

sm2 = di_container.get_settings_manager()

print(sm1.settings())
print(sm2.settings())
