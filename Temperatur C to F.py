#A program to convert temperature from degree celcius to Degree farenheit.
# By Jay Monpara
def Main():
        print
	Celcius = input("What is the temperature in celcius?") # provoke user to input celcius temperature.
	Fahrenheit = (9.0/5.0) * Celcius + 32 # process to convert celcius into fahrenheit
        print
	print "The temperature is", Fahrenheit,"degrees fahrenheit." # dispalys the output
        print
        if Fahrenheit >= 90: # conditonal statement
            print "It's really hot out there, be careful!"
        if Fahrenheit <= 30:
            print "It's too cold out there. Be sure to dress warmly"
Main()


