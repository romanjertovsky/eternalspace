from output import msg_out


def greeting_screen():

    welcome_text = """Hello. Welcome to the...
                                                                            
@@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@   @@@  @@@   @@@@@@   @@@        ,!    
@@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@     -- -+ - -
@@!         @@!    @@!       @@!  @@@  @@!@@@@@  @@!  @@@  @@!         | '  
!@!         !@!    !@!       !@!  @!@  !@! @!@!  !@!  @!@  !@!              
@!!!:!      @!!    @!!!:!    @!@!!@!   @!@ @!@!  @!@!@!@!  @!!              
!!!!!:      !!!    !!!!!:    !!@!@!    !@! !@@!  !!!@!!!!  !!!       ;      
!!:         !!:    !!:       !!: :!!   !!:  !@!  !!:  !!!  !!:   - --+- -   
:!:         :!:    :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:       '      
::: ::::     ::     :: ::::  ::   :::   ::   ::  ::   :::  :: ::::          
: :: ::      :     : :: ::    :   : :  ::    :    :   : :  : :: : :         
                                                         .               +  
                                                         :            .     
 @@@@@@   @@@@@@@    @@@@@@    @@@@@@@  @@@@@@@@         !        .         
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@         |_         +       
!@@       @@!  @@@  @@!  @@@  !@@       @@!           ,  | `.               
!@!       !@!  @!@  !@!  @!@  !@!       !@!   - --- --+-<O>-+- ---  --  -   
!!@@!!    @!@@!@!   @!@!@!@!  !@!       @!!!:!        `._|_,'               
 !!@!!!   !!@!!!    !!!@!!!!  !@!       !!!!!:           Y                  
     !:!  !!:       !!:  !!!  :!!       !!:       +      |                  
    !:!   :!:       :!:  !:!  :!:       :!:              !                  
:::: ::   !::       ::!  :::   !::::::  :: ::::          :         . :      
:: : :     :         :   : :   :: :: :  : :: ::          .       *          """

    msg_out(welcome_text, 'b')


def beginning_of_the_story():
    msg_out('...', 'b', 2)
    msg_out('......', 'b', 1)
    msg_out('.........', 'b', 0.5)
    msg_out('You woke up after hibernation in your spaceship on unknown planet.', 'b', 7)
    msg_out('You do not know where you are.', 'b', 5)
    msg_out('How did you get here?', 'b', 4)
    msg_out('You do not remember anything.', 'b', 4)
    msg_out('You do not remember where you came from, time, or your name...', 'b', 6)
    msg_out('You see only the flickering display of control terminal in your spaceship... What you will do?', 'b', 7)
    msg_out('Now everything that happens depends only on you!', 'b', 9)
    msg_out('Or not?...', 'b', 2)
