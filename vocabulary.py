# Our vocabulary of words
glossary = {
    "algorithm": "(noun) a step-by-step procedure to achieve a specific goal. Can be implemented with code.",
    "argument": "(noun) a value that is passed into a function when it is called. Arguments are said to be “passed” "
                 "into a function, and functions are said to “take” arguments. Also known as a “parameter.”",
    "array": "(noun) a type of value that contains a sequence of other values.",
    "assignment": "(noun) the act of putting a value into a variable.",
    "brackets": "(noun) characters often used to surround text.",
    "bug": "(noun) a mistake in a program.",
    "call": "(verb) to run the code in a function. Also referred to as “running,” “executing,” or “invoking” a "
            "function.",
    "class": "(noun) a type that can be defined by the programmer. Classes are defined in order to create objects of "
             "that class. ",
    "comment": "(noun) arbitrary text written around code, but which is never run, and is generally ignored by the "
               "computer. Used to leave notes and documentation for people who read the code later. Also used to stop "
               "code from running",
    "comment out": "(verb) to turn code into a comment so that it does not get run.",
    "compiler": "(noun) a program that converts code into an executable, and checks that the syntax is correct. "
                "Sometimes compilers convert code into other code.",
    "constant": "(noun) a variable that never changes its value",
    "crash": "(verb) to cause a running program to stop due to an error.",
    "data structure": "(noun) a value that contains other values.",
    "debug": "(verb) to investigate and fix bugs.",
    "declaration": "(noun) code that declares that something exists – usually a variable, function or a class.",
    "definition": "(noun) code that fully implements something – usually a variable, function or a class. ",
    "double": "(noun) a float that can represent a wider range of numbers than a normal float.",
    "execute": "(verb) Synonym for run.",
    "executable": "(noun) a program, usually a single file, ready to be run.",
    "float": "(noun) a type of value that represents numbers with fractional parts. Short for “floating-point number”.",
    "function": "(noun) a piece of code that is not run until it is called. Functions take zero or more arguments. "
                "When a function finishes running, it returns a return value back to the code that called it.",
    "function call": "(noun) code for calling a function. Function calls specify which function to call, and all of "
                     "the arguments that the function requires. The result of a function call is a return value. Not "
                     "all functions have a return value.",
    "implement": "(verb) to write all the code to complete something – usually a function or a class.",
    "instance": "(noun) Synonym for object.",
    "instance variable": "(noun) a variable that is attached to an object. Also known as a “member variable” or just "
                         "a “member.”",
    "instantiate": "(verb) to create an object from a class.",
    "integer": "(noun) a type of value that represents whole numbers.",
    "interpreter": "(noun) a program that runs code. For languages that are not compiled, the source code is run "
                   "directly by an interpreter.",
    "invoke": "(verb) Synonym for call.",
    "iterate": "(verb) Synonym for loop.",
    "loop": "(noun) a piece of code that runs itself repeatedly. Commonly used to run a piece code for every value in "
            "an array. Also known as “iteration”.",
    "member function": "(noun) Synonym for method.",
    "member variable": "(noun) Synonym for instance variable.",
    "method": "(noun) a function that is attached to an object. Methods belong to, and are defined in, a class. Also "
              "known as a “member function.”",
    "nested": "(adjective) contained within something like itself. E.g. a nested array is an array that is inside"
              " another array, and a nested class is a class defined inside the definition of another class.",
    "object": "(noun) a value created from a class.",
    "object-oriented": "(adjective) designed using objects.",
    "parameter": "(noun) Synonym for argument.",
    "parenthesis": "(noun) A type of bracket",
    "procedure": "(noun) Synonym for function.",
    "program": "(noun) a full piece of software that is ready to be run. Usually an executable.",
    "read": "(verb) to retrieve input data values from an external source – usually from a file. Can refer to "
            "retrieving data over a network, such as the internet. The opposite of writing.",
    "return": "(verb) to immediately stop a called function from running, possibly providing a return value.",
    "return value": "(noun) the value that results from a completed function call.",
    "run": "(verb) to perform the instructions written in code or an executable. Code is a set of instructions, and "
           "“running” code is when the computer actually performs those instructions. To “run” a function means to"
           " call that function.",
    "string": "(noun) a type of value that represents text. The word “string” derives from the phrase “string of "
              "characters.”",
    "syntax": "(noun) the grammatical rules of a programming language.",
    "type": "(noun) the kind or category of a value. Every value has a type.",
    "value": "(noun) a piece of data that can be contained inside a variable. Every value has a type. ",
    "variable": "(noun) a named container for a single value. Variables are not values themselves, they are merely "
                "containers for values. ",
    "write": "(verb) to send output data values to an external destination – usually to a file. Can refer to sending "
             "data over a network, such as the internet. The opposite of reading.",
    "bit": "a single binary piece of data, either a 0 or a 1.",
    "byte": "eight bits strung together to represent a specific value such as a letter or a digit.",
    "dword": "a double word, or 32 bits.",
    "nibble": "a half byte, or 4 bits.",
    "word": "16 bits of data used to represent a discrete piece of data.",
    "emoji": "another word for emoticon, it’s those little smiley faces, frowning faces, tables, etc. that are used to "
             "convey tone or emotion in written conversations.",
    "spam": "We may never have the absolute and authoritative explanation of why junk email is called spam. Some say "
            "it’s because you can liken email to ham, and not important email (junk and adverts) as spam, which is not "
            "really purely ham. I prefer to give credit to another Monty Python fan.",
    "mouse": "what else could you expect Doug Englebart and Bill English to call their small device with a tail coming "
             "out of it, an X-Y position indicator? Fortunately their word for the cursor, bug, didn’t catch on like "
             "their invention the mouse. You can even buy mice that look like mice.",
    "twain": "a standard for hardware interoperability, this was originally a type of technology without an interesting"
             " name, until someone was inspired by Rudyard Kipling to borrow from the Ballad of East and West, since it"
             " seemed that “…never the twain shall meet.”",
    "hashtag": "the # character (called an octothorpe) combined with a word or phrase that concisely defined a "
               "conversation, post, tweet, or image into a category, intended to make it easier for people to find by "
               "searching on the term associated with the hashtag. Brought into larger awareness by Jimmy Fallon and"
               " Justin Timberlake.",
    "like": " in this case, we have Facebook to thank for the thumbs up icon that users can click to indicate they "
            "like/support/are in favor of someone’s post. Used in the vernacular, it is a concise way to express "
            "agreement.",
    "poke": "another term with common origins in Facebook, poking someone is a way to remind them that they are "
            "involved in the community, but have not interacted in an extended period of time. It sounds like a lewd"
            " act to anyone not familiar with it.",
    "troll": "Like the humanoid that lives under bridges and preys upon the weak and innocent, trolls lurk in discussio"
             "n groups or on social media websites and live only to post inflammatory statements or to ridicule and der"
             "ide others. Trolling is the verb to define such actions.",
    "tweet": " A post to Twitter is called a tweet, and the act of submitting a post is called tweeting.",
    "blob": "A blob is a Binary Large Object, and indicates some large amount of data other than just simple text, usu"
            "ally stored within a database.",
    "crapplet": "An applet, usually Java based, that is not worth anything.",
    "dead Tree": "A paper printout of an electronic file; frequently done single-sided and in color.",
    "easter Egg": "Stemming from the ages-old tradition of hiding colorful eggs for children to seek out, programmers"
                  " may also embed Easter Eggs in their programs for motivated hackers to find. ",
    "gui": " A gooey is a Graphical User Interface, and not something that requires hand-sanitizer, but try talking a"
           "bout your GUI around non-techies and see what facial expressions result.",
    "hardcopy": "like Dead-Tree above.",
    "hash": " A hash is a fixed-length numerical value calculated from a variable length amount of data, and can be u"
            "sed to validate the authenticity or to detect tampering with data.",
    "thunking": " When a program must call a subroutine to complete a task, it is called thunking. In Windows, when a"
                " 64-bit operating system must downshift into 32-bit mode for legacy code, or a 32-bit version must "
                "run old 8-bit code, it is also called thunking. You can almost hear the processor grinding.",
    "virus": " In nature, a virus is a primitive life-form that exists only to replicate itself, consuming resources"
             " from a host to manufacture more of itself. It is this behavior that led to code that not only does th"
             "is, but also causes damage, steals data, and can provide attackers with remote access to victim machines "
             "coming to be known as a virus.",
    "warez": " All 1337 speakerz replace the letter S with Z, use pidgin grammar, and shorten wordz, so “warez” is shor"
             "t for “softwares” and refers to ill-gotten gains, either pirated, cracked or being used with a key"
             " code to circumvent licensing requirements.",
    "worm": "A software worm crawls across systems, either seeking specific data or exploiting vulnerabilities "
            "which can in turn be used to exploit other systems. Unlike a virus that must be executed by a sys"
            "tem, a worm seeks to exploit the system through externally accessible vulnerabilities a"
            "nd does not require user interaction.",
    "404": "The HTTP response code for “File Not Found”, 404 is being used to simply convey things like “not found,” “n"
           "ot here,” or even “I don’t know.”",
    "cookies": "Small files used to store state from one visit to a next, cookies are also being used to track "
               "users and deliver advertising. Anything that indicates where you have been or what you have done may no"
               "w be referred to as a cookie, including phone logs and footprints.",
    "wiki": " A backronym was coined to say Wiki stands for “What I Know Is” but it is actually Hawaiian for “quick.”",
    "afk": "Away From Keyboard",
    "ama": "Ask Me Anything",
    "boss Key": "Any key built into a game that quickly pauses the game and brings up a spreadsheet or other screen tha"
                "t looks like work so your boss doesn’t realize you were goofing off.",
    "cki": "Refers to an error in the Chair Keyboard Interface. Think about what connects the chair to the keyboard.",
    "crack": "To compromise or suborn a piece of software, website, or remote system with malicious intent.",
    "fubar": " From an old military jargon term, this means “Fouled Up Beyond All Repair,” or at least close enou"
             "gh to that so my editor won’t get mad at me.",
    "hack": "o improve, reverse engineer, adapt for other purposes, or suborn a piece of hardware or software"
            ", website, or remote system for the purposes of learning more or expanding capabilities.",
    "id10t": "Another error, usually sounded out as Aye-Dee-Ten-Tee but seldom written as it should be pretty o"
             "bvious what is being said.",
    "interwebs": "Slang for the Internet, as a way to poke fun at non-technical people who confuse the Internet with t"
                 "he World Wide Web.",
    "irl": "In Real Life",
    "kludge": "A poorly programmed piece of software, a piece of hardware cobbled together from spare parts, or a proj"
              "ect plan created by someone with no real experience with the task at hand.",
    "kos": "From gaming, it stands for Kill On Site and can also be used to indicate data to be deleted or hardware t"
           "o be retired.",
    "lmao": "Laughing My A** Off",
    "lmfao": "Laughing My Freaking A** Off",
    "lol": "Laugh Out Loud",
    "lulz": "Another variant on expressing humor",
    "n00b": "Spelled with zeroes, it indicates a relative newcomer or someone lacking experience.",
    "pebkac": "Another helpdesk acronym that indicates the Problem Exists Between the Chair and the Keyboard, li"
              "ke a CKI error.",
    "podcast": "Not just for iPods anymore, a podcast is any recorded media that can be consumed later and can cove"
               "r virtually any topic. Podcasts are usually under an hour or so, usually audio only, and consist of a"
               " lecture, dialog, or interview on a particular topic. Many podcasters create regular programs with a u"
               "nifying theme.",
    "pr0n": "Also spelled with a zero and with intentional shifting of positions, it stands in the place of porn to in"
            "dicate pornography, and was probably coined as an attempt to get around simple word filters.",
    "pwn": "Gaming term for “own,” indicating that when one player pwns another, he or she has soundly defeated his "
           "or her opponent.",
    "rofl": "Rolling on the floor laughing",
    "rotflmfao": "Rolling on the floor laughing your freaking a** off",
    "snafu": "Situation Normal, All Fouled Up, or close enough you get the gist. SNAFUs can be one word status report"
             "s, sit-reps, or responses to “sup?”",
    "sneakernet": "The old-fashioned way of transferring data using external, portable media by copying the data to "
                  "disk and then walking it over somewhere.",
    "teh": "Whether it’s poor typing skills or just a way to be cool, “Teh” stands in for “The” but can also indicate e"
           "mphasis.",
    "tubez": "Thanks to US Senator Ted Stevens, whose famous address on Net Neutrality showed conclusively that just b"
             "ecause you chair a committee in charge of something, doesn’t mean you actually know anything about it, “"
             "the tubez” complete with the Z in place of the S will go down as one of the US government’s most embarr"
             "assing contributions to the technology they helped start.",
    "troubleshoot": "to try to find the cause of a product or system not working correctly, especially one involving a "
                    "piece of equipment or machine, and try to find the solution"
}