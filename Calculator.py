# @Robert McElhinney (ID ....)
# @Paul Ryan (ID INPUT HERE)

from tkinter import *
from IOPanel import *
from Digit import *
from GridPositioner import *
from Stack import *

# Class for a GUI-based calculator.
class Calculator( Tk ) :
    # Width of @IOPanel@ in pixels.
    __IO_PANEL_WIDTH = 200
    # Height of @IOPanel@ in pixels.
    __IO_PANEL_HEIGHT = 50
    # Row number of @IOPanel@ in grid layout of the calculator.
    __IO_PANEL_ROW = 0
    # Column number of @IOPanel@ in grid layout of the calculator.
    __IO_PANEL_COL = 0
    # Span of @IOPanel@ in widgets in the grid layout of the calculator.
    __IO_PANEL_SPAN = 3

    # The number base of the calculator.
    __BASE = 10

    # The title of this calculator's window.
    __TITLE = "Calculator"

    # Row number of the first digit row in grid layout of the calculator.
    __DIGIT_ROW = 1
    # Column number of the first digit row in grid layout of the calculator.
    __DIGIT_COL = 0
    # Number of digit buttons per row in grid layout of the calculator.
    __DIGITS_PER_ROW = 3

    # Text on the clear button.
    __CLEAR_TITLE = "C"
    # Text on the push button.
    __PUSH_TITLE  = "P"
    # Text on the add button.
    __ADD_TITLE = "+"
    # Text on the substraction button.
    __SUB_TITLE = "-"
    # Text on the multiplication button.
    __MUL_TITLE = "*"
    # Text on the division button.
    __DIV_TITLE = "/"
    # Text on the unary minus button.
    __UMIN_TITLE = "(-)"

    # Main constructor.
    #  @parent@: The master widget of this @Calculator@ or @None@
    #  @base@: The number base for this @Calculator@.
    def __init__( self, master, title=__TITLE, base=__BASE ) :
        # Initialise main calculator window.
        Tk.__init__( self, master )
        # Set title.
        self.title( title )
        # Save @master@. Not used...
        self.__master = master
        # Finish rest of initialisation.
        self.__initialise( base=base )
        # YOU SHOULD REMOVE THIS. IT'S FOR DEMONSTRATING THE API.
        #self.__iopanel.set( "HI" )

    # Utility method for initialising this @Calculator@'s components.
    #  @base@: the number base of this @Calculator@'s operations.
    def __initialise( self, base ) :
        # Initialise the IO panel component.
        self.__initialiseIOPanel( )
        # Initialise the digit panel component.
        self.__initialiseDigitPanel( base=base)
        stack = Stack()
        self.stack = stack

    # Initialise the digit panel widget of this @Calculator@.
    #  @base@: the number base of this @Calculator@'s operations.
    #  @row@: row number in grid layout of this @Calculator@.
    #  @col@: column number in grid layout of this @Calculator@.
    #  @digitsPerRow@: digits per row in grid layout of this @Calculator@.
    def __initialiseDigitPanel( self,
                                base,
                                row=__DIGIT_ROW,
                                col=__DIGIT_COL,
                                digitsPerRow=__DIGITS_PER_ROW ) :
        appendee = self.__iopanel
        self.__base = base
        self.__positioner = GridPositioner( row=row, col=col, columns=digitsPerRow )
        for digit in [ digit for digit in range( 1, base ) ] + [ 0 ] :
            button = Digit( master=self, digit=digit, appendee=appendee )
            self.__positioner.add( button )
        # Adds a button for the clear function.
        self.__addSpecialDigitPanelButton( text=Calculator.__CLEAR_TITLE,
                                           command=self.__onClearButtonClick )
        # Adds a button for the push function.
        self.__addSpecialDigitPanelButton( text=Calculator.__PUSH_TITLE,
                                           command=self.__onPushButtonClick )
        # Adds a button for the addition function.
        self.__addSpecialDigitPanelButton( text=Calculator.__ADD_TITLE,
                                           command=self.__onAddButtonClick )
        # Adds a button for the subtraction function.
        self.__addSpecialDigitPanelButton( text=Calculator.__SUB_TITLE,
                                           command=self.__onSubButtonClick )
        # Adds a button for the multiplication function.
        self.__addSpecialDigitPanelButton( text=Calculator.__MUL_TITLE,
                                           command=self.__onMulButtonClick )
        # Adds a button for the division function.
        self.__addSpecialDigitPanelButton( text=Calculator.__DIV_TITLE,
                                           command=self.__onDivButtonClick )
        # Adds a button for the unary minus function.
        self.__addSpecialDigitPanelButton( text=Calculator.__UMIN_TITLE,
                                           command=self.__onUMinButtonClick )

    # Utility method for adding additional button to the digit panel.
    #  @text@: the text on the button.
    #  @command@: the button's callback method.
    def __addSpecialDigitPanelButton( self, text, command ) :
        button = Button( master=self, text=text, command=command )
        self.__positioner.add( button )

    # Initialise the IO panel widget of this @Calculator@.
    def __initialiseIOPanel( self ) :
        width = Calculator.__IO_PANEL_WIDTH 
        height = Calculator.__IO_PANEL_HEIGHT
        # create the IO panel.
        iopanel = IOPanel( master=self, width=width, height=height )
        row = Calculator.__IO_PANEL_ROW
        col = Calculator.__IO_PANEL_COL
        span = Calculator.__IO_PANEL_SPAN
        # Add the IO panel to the current crid layout.
        iopanel.grid( row=row, column=col, columnspan=span )
        # Save object reference to the IO panel for future use.
        self.__iopanel = iopanel

    # Callback method for push button.
    def __onPushButtonClick( self ) :
        if self.__iopanel.get() != None:
            #if the base is between 2 - 9, convert it to base ten.
            if self.__base in range(2,9):
                self.stack.push(self.stack.convertToDecimal(self.__iopanel.get(), self.__base))
            #if the base is 10 then push it to the stack.
            else:
                self.stack.push(self.__iopanel.get())
        # Clear the iopanel input.
        self.__iopanel.reset( )
        

    # Callback method for clear button.
    def __onClearButtonClick( self ) :
        self.__iopanel.reset( )
    # Callback method for push button.
    def __onAddButtonClick( self ) :
        self.__iopanel.reset( )
        # Sets the output to the added result.
        self.__iopanel.set(self.stack.add(self.__base))
    # Callback method for subtraction button.
    def __onSubButtonClick( self ) :
        self.__iopanel.reset( )
        # Sets the output to the subtracted result.
        self.__iopanel.set(self.stack.subtract(self.__base))
    # Callback method for multiplication button.        
    def __onMulButtonClick( self ) :
        self.__iopanel.reset( )
        # Sets the output to the multiplied result.
        self.__iopanel.set(self.stack.multiply(self.__base))
    # Callback method for division button        
    def __onDivButtonClick( self ) :
        self.__iopanel.reset( )
        # Sets the output to the divided result.
        self.__iopanel.set(self.stack.division(self.__base))
    # Callback method for unary minus button
    def __onUMinButtonClick( self ) :
        # Creates a new integer which is equal to the negative of the
        # value of the operand.
        um = int(self.__iopanel.get( )) * -1
        # Resets the user inputted value
        self.__iopanel.reset()
        # Sets the iopanel input equal to the negative of the given
        # user inputted value.
        self.__iopanel.append(str(um))
             
    

if __name__ == "__main__" :
     calculator = Calculator( None )
     calculator.mainloop( )
