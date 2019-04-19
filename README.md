# Yosh
a python data saving system


Not use "@" and "=" as keys, category or values
Using comming soon

## Setup
    import YoshData

    With file
    yosh = YoshData.File(file="FileLocation")
    
    With the string
    YoshData.File(string="YoshString")
    
Instert values
----------------------

    # Write (File Only)
    # Add value with saving
    yosh.write("key", "category", "value")
    
    # Add
    # Add value without saving
    yosh.add("key", "category", "value")

Read value
----------------------
    
    # getValue
    # return the normal value
    v = yosh.getValue("key", "category")
    
    # getValueAsInt
    # return the value as integer
    v = yosh.getValueAsInt("key", "category")
    
    # getValueAsStr
    # return the value as string
    v = yosh.getValueAsStr("key", "category")
    
    
    # getKeyValues
    # return the key dictionary
    v = yosh.getKeyValues("key")


Saving
----------------------
    # Read
    # returns the used yosh dictionary as a saveable string
    dictionary = yosh.read()
    
    # Save (File Only)
    # save current yosh dictionary
    yosh.save()
    
    
File structure
----------------------
    @key="KeyName" @category="Value" @category="Value" 
    @key="KeyName" @category="Value" @category="Value" @category="Value" 
    
    example
    
    @key=Car @doors=3 @description=A Red Car
    @key=Recipe1 @for=Cookies @need=go to a shop
    
    example for user datas
    @key=1 @name=Max @age=27 @like=cookies @car=yes @nick=Best Max
    @key=2 @name=Juile @age=24 @tel=0123-123111 @gender=female
    
