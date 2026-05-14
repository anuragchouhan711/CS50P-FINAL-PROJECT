    # Solar System Simulator
    #### Video Demo:  <https://youtu.be/I6yJVc8GMJM>
    #### Description:
        Into:
        In this project I tried to create a smalled down version of solar system in which planets postion are updated constantely.
        This has a Time and planet revolution counter which give roughly similar planets revolution with time to their actual time,
        also it has other features like speed control to increase / decrease revolution speed and timer to control how much years
        you want it to run and ofc the Time is in terms of our convention measure of years that is revolution of Earth.
        I've first tried to use print and clear for every frame by the os library with os.system('clear') which was very hard to run
        and become heavier to run with as i progress , then mid project i switched to curses library which was much better for this
        project and made the program effortless to run and the fps increased a lot .
        Also i was using list first to store the cordinates of orbit and it was causing me a lot of performance as going through list
        to see if a cordinate exist if its or it dosent exist and mutiple copy , swithching to set solved the issue.
        When starting the project i fixed the cx and cy so the solar sytem always stays in same place for everyone but later i realise
        that everyone can have a diffrent terminal size and display so i made it so its always project the system in centre of the screen
        of everyone .

    TODO

    Features and how to run it:
        You can set which planet/s you wanna see , the default is all planets if no planet/s is specified.
                To set custom planet you use the argument -p __ followed with planet names.
                (NOTE: It can only be done when starting new instance the program.)



        Ive put up a timer , it runs till Time has reached 99999 years so it dosent run forever ,
        tho you can set the time to custom years .
            (NOTE : Time only works with Earth referece like in real
                if the the Earth is not selected, Time would say "NO refrence cause earth dosen't exist!")



        You can also set the speed at which planets rotate .You can set the default speed while starting the program
            with argument -s __ followed by the speed
            (Note:The default speed is 0.1 , and the range allowed is from 1 to 0.001 ,the lower the value the faster time goes.)

        You can increase the speed while the program is running by pressing "+/=" key to increase the speed ,
            and "-/_" key to decrease the speed.



        To run the program you need a minimum terminal size , the program won't start if the terminal dosent meet the minimum required size.
            (NOTE: If terminal size is change after the program has started and change to below minimum required size the program will stop with the
                message as followed "Terminal size too low! , Increase size to continue" , you can increase the size to continue. )


    TO STOP THE SIMULATION :
        Press: ctrl + c

    It might not be the biggest or the most complex project i could have build but i like space a lot and i have learned a lot about data structures and
    why its important to manage them efficiently , while writing manytimes i did something which made the whole thing run like 1 fps in 8 seconds .
    Also studying about planets revolution was fun and it was quite a challange converting it to feasable size and time . 
