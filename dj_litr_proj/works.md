Извини, при написании скрипта допускал ошибки. 
Забыл обнулить автоинкремент,
в поле `created_at` оставил сегодняшнюю дату,
переборщил с количеством записей
и ценой книг при заполнении.
Относительно поздно спохватился и экономя время продолжил работу и поставил лимит в некоторых запросах


### Базовые фильтры
1. Найди всех авторов с именем «John».  
In [1]: list_author = Author.objects.filter(first_name='John')
In [3]: for a in list_author:
   ...:     print(a)
   ...: 
John Smith - statementjackhardy@example.org
John Johnson - guycomptonmelissa@example.org
John Bates - writerthomas53@example.net
John Lewis - racemevans@example.org
John Moore - ageamanda59@example.net
John Kane - bodyjohnsonalexandria@example.net
John Williams - thatlori90@example.com
John Wilson - nightchandlermadison@example.com
John Owens - adddennisspencer@example.org
John Kemp - considergoodmanandre@example.org
John Abbott - soongarrettgonzalez@example.org
John Romero - voicerogersmark@example.org
John Murray - researchhshea@example.net
John Martin - Mrsujohnson@example.net
John Flores - businessbellis@example.net
John Page - approacheringalvan@example.com
John Kim - setxmeadows@example.net
John Ross - downawade@example.org
John Stanley - considermserrano@example.net

2. Найди всех авторов, кроме тех, у кого фамилия «Doe».
In [6]: list_author = Author.objects.exclude(last_name='Doe')
In [7]: for a in list_author:
   ...:     print(a)
   ...: 
Richard Harrington - sharetuckeromar@example.net
Anne Richardson - loseobrienmichael@example.net
Douglas Li - smilexjuarez@example.org
Bonnie Peterson - yardstephaniemorris@example.com
Denise Lopez - politicalstephanie92@example.net
Samuel Gomez - rateocarr@example.net
Philip Sanders - comparethompsoncathy@example.org
Margaret Pena - purposebridgetdavis@example.org
Holly Camacho - airjohnstephens@example.org
Thomas Johnson - believeevan75@example.net
Tina Lopez - usuallychristina91@example.com
Jacob Dennis - everybodyhbryant@example.net
Jennifer Thompson - preparewilliamsmith@example.org
David Morse - benefitkenneth47@example.com
Alisha Blanchard - sameashley15@example.org
Deborah Jones - northqgarrett@example.org
Dustin Moore - maybeswhite@example.com
Mark Figueroa - newssharonbyrd@example.com
Steven Butler - factorlgreene@example.org
Timothy Russell - ballbward@example.org
James Lewis - choosefrankkenneth@example.net
Jonathan Dixon - serioustamarafisher@example.net
Patricia Olson - knowamartin@example.net
Robert Hall - nightzgardner@example.com
Derek Lopez - forcejames90@example.net
John Smith - statementjackhardy@example.org
Wayne Bryan - executivejenniferharris@example.org
Nicholas Pineda - wouldjamesyoung@example.org
Lisa Ford - informationsanderson@example.com
Megan Snyder - collectionmatthew41@example.net
Jeffrey Smith - wrongimiller@example.org
Walter Mercado - productkarenkramer@example.com
Matthew Greene - timermedina@example.org
Cynthia Little - legcynthia36@example.com
Christopher Rogers - billamberjones@example.com
Nicholas Rodriguez - leastlisalopez@example.com
Amy Lee - suremichael21@example.com
Desiree Anderson - managebrownsarah@example.org
Ann Huynh - treatmentvargasmelissa@example.org
Elizabeth Conrad - itsaustinpeterson@example.org
Douglas Hawkins - southernjennifermiller@example.org
Jared Walker - threetaylor61@example.org
Christina Gutierrez - bagshane45@example.com
Kristie Cook - bigkennedykyle@example.com
Andrea Arnold - cityrhill@example.org
Ashley Cox - standbstone@example.com
Cory Hammond - developmentoconnellnicole@example.org
Andrea Johnson - carryericgomez@example.com
Justin Larsen - manageruizcassandra@example.org
Matthew Rhodes - materialkellybrown@example.net
Curtis Lowe - takecarla41@example.com
Lisa Miller - butpamela19@example.org
Taylor Bradley - ajeffery15@example.com
Gary Hernandez - helpmariadavis@example.com
Karen Gutierrez - tableeduardoperry@example.net
Michael Greer - discussemily31@example.com
Clayton Davis - nextdanielsjimmy@example.org
Diana Peck - manbhaney@example.com
Alicia Baker - leaderamanda91@example.net
Wayne Peterson - leftvbrown@example.org
Matthew Riddle - cutidouglas@example.net
Edward Perkins - speakcherylramos@example.net
Richard Brown - latercaitlinsalazar@example.com
Michelle Rios - losewhiteanita@example.org
Michele Williamson - strongjosephjones@example.org
Brianna Mccoy - majorwesley77@example.com
John Johnson - guycomptonmelissa@example.org
Danielle Wells - generalybell@example.net
Chad Dunn - investmenturamos@example.net
Jennifer Robinson - officejason21@example.com
Brian Wheeler - lookrebecca76@example.com
James Hicks - voicegreerselena@example.net
Jared Fernandez - workermanntonya@example.com
Leslie Roy - structurecodylawrence@example.com
Jennifer Krueger - linejason82@example.com
Jonathan Howard - fivefortiz@example.org
Veronica Miller - measurekimberlymcneil@example.com
Amber Cross - imaginejpennington@example.org
Marco Owens - guessrobinking@example.net
Amy Hinton - nearlyronalddavis@example.net
Cody Garner - socialbryanwilliams@example.com
Scott Sanders - landwfranco@example.net
Joanna Morris - himselfrobertwalker@example.com
Sandra Scott - pricehwilson@example.org
Claudia Jones - nationalbrogers@example.org
Matthew Moore - ableiscott@example.net
Harry Cordova - ownbrianruiz@example.org
John Bates - writerthomas53@example.net
Melissa West - speakkevinmurray@example.org
Lori Carr - languagejeffrey49@example.net
Catherine Martin - storycourtneysingh@example.net
Cindy Payne - betweenmaciaspaula@example.com
Sharon Velez - sellalvaradolaura@example.net
Brittany Harding - explainlisa82@example.org
Patricia Haynes - reducesmithjeffrey@example.com
Jill Rodriguez - helpbakersamantha@example.net
Brandon Cox - thirdantonio94@example.org
Jennifer Chan - attentionmccoykevin@example.net
Amber Lee - clearsara19@example.org
Sandra Davis - mechadthompson@example.org
Megan Williams - wordgeorgebrown@example.net
Jessica Duncan - actuallymanuelmontgomery@example.com
Breanna Clarke - betterpetersonkristina@example.com
Larry Boyle - tonightjasonsmith@example.org
John Lewis - racemevans@example.org
Terri Kennedy - stayfmoore@example.com
Aimee Duffy - imaginejenningslydia@example.net
Teresa Green - militarydiana09@example.org
Megan Schaefer - singlemyersmark@example.org
Raymond Gonzales - variouscrystal74@example.org
Kayla Rodriguez - employeebarnettjohn@example.net
Randy Rodriguez - expectjlloyd@example.org
Lori Morris - largehubbarddanielle@example.org
Brian Yates - partpaul70@example.com
Robert Figueroa - learnkristaramos@example.com
David Hicks - withoutalexander75@example.net
Andre Ellison - betterpshaffer@example.org
Tiffany Alvarado - businessopayne@example.com
Alexander Miller - ownjrodriguez@example.com
Nathan Rosario - caresheakathleen@example.org
Patricia Alvarez - hardcarmenbush@example.org
Barbara Wiggins - collegencampos@example.net
Tammy Melton - waterpatrick25@example.org
Joshua Watson - containwallacebrandy@example.org
Fernando Perkins - programjonathan64@example.net
Zachary Moore - financialscottmays@example.com
Michelle Owen - wrongericrobinson@example.net
Emily Zimmerman - hopegreenbenjamin@example.com
Joshua Thomas - saveandersonleslie@example.org
Debbie Bennett - agoxthompson@example.net
Nathan Gates - arobert19@example.org
Lisa Wells - basejoshuacooper@example.com
Shawn Middleton - measureelizabethstokes@example.com
Jeremy Lewis - leavebeverly63@example.net
Robert Jackson - practicepattersonjames@example.com
Crystal Banks - sistergoldenleslie@example.com
Hannah Moore - dinnermatthew74@example.com
John Moore - ageamanda59@example.net
Kathleen Johnston - sourceandrew33@example.com
Martin Hansen - heartpattersongarrett@example.net
Drew Myers - theorywilliamstammy@example.org
Timothy Patel - updfrederick@example.org
Andrew Allison - memoryxavier95@example.com
Amber Crawford - dogdaniel39@example.com
Steven Bowers - bedjose17@example.org
Aaron Johnson - frontgabrielbarber@example.net
Robert Becker - degreesarayang@example.org
Shaun Wilson - policykeith38@example.com
Johnathan Ponce - anysherrysimmons@example.net
Patricia Williams - sitegrantdale@example.net
Beth Allison - theyiwallace@example.com
John Kane - bodyjohnsonalexandria@example.net
Jennifer Lawson - roommooreanthony@example.com
Mark Lewis - factrmata@example.org
Jessica Vaughn - audienceimontoya@example.net
Rachel Edwards - losshaynesapril@example.net
Monica Oliver - morningmatthewowens@example.org
Donald Middleton - authorityantonio91@example.com
Colleen Roberts - sourcecarlsonchristopher@example.com
Jamie Russell - seniorucampos@example.org
Michael Bowen - coldbrowneugene@example.org
Sarah Montes - truthheather87@example.net
Shelly Williams - travelteresamatthews@example.net
Lisa Garrison - newspaperflynnjoseph@example.net
Lee Moore - pastkara82@example.org
Patricia Koch - yourickey05@example.net
Eric Lee - winclarkdeanna@example.com
Leslie Shaw - enjoymaysjacob@example.com
Lisa Baldwin - trainingandersontyler@example.com
Jim Kennedy - particularholly40@example.com
Holly Young - thanklopezshawna@example.org
Daniel Middleton - recentgallison@example.net
Ann Johnson - challengedawnholland@example.com
Michelle Moore - foreignxleonard@example.com
Linda Martinez - officialphillipsdavid@example.com
Monica Boyd - mindsamanthahall@example.net
James Cardenas - factoroy@example.net
Bonnie Bowman - reallyhwatson@example.net
Michael Roberts - safewilliam61@example.com
Donna Bell - structuredavidsantiago@example.com
Lori Johnson - newspaperlwoods@example.net
Kimberly Richmond - sendrwashington@example.org
Kevin Matthews - thanromeroeileen@example.net
Richard Burke - insidelauren15@example.com
Raymond Mccormick - firestoneblake@example.com
Tabitha Hernandez - studyalan06@example.com
Emily Bennett - gameambermiller@example.com
Robert Chen - individualkimberly83@example.net
Charles Green - footemorales@example.org
Peter Brewer - rangehernandezdavid@example.net
Jeremy Stewart - everytoddnancy@example.net
Sarah Hicks - maintainjonathan87@example.com
Steven Becker - springjacksonangela@example.org
Sue Gutierrez - wearcharles32@example.net
Amanda Vazquez - betweenkyle27@example.com
Daniel Stone - magazinebenjaminsaunders@example.com
Michael Smith - spacekristen00@example.net
Angela Williams - wayokramer@example.com
Kaitlyn Mccall - shoulderharperjoseph@example.com
John Williams - thatlori90@example.com
Jerry Gibson - followangelasexton@example.net
Janet Page - doctorkgaines@example.net
Melody Ward - theselisamartin@example.org
Manuel Greene - meetmatthew38@example.org
Robert Allen - believelambsara@example.org
Daniel Weber - drophannahyoung@example.org
Tonya Hernandez - firmqkennedy@example.net
Tom Gillespie - ourjonathan93@example.net
Gary Miller - himselfzachary79@example.net
Victoria Morgan - sevenlisaparker@example.com
Monica Hardin - nightpyoung@example.net
Paul Webster - whilepalmersierra@example.com
Brittney Johnson - todayobrienvanessa@example.com
Kristin Hunt - goalvhebert@example.com
Holly Lopez - thinkajackson@example.org
Carrie Moore - returnewest@example.net
Lisa Decker - fightmbarnett@example.net
Sandra Smith - insidehgray@example.org
Carlos Larson - politicalashley02@example.org
Michael Hunter - allrobert05@example.com
Jeffrey Burch - perautumn96@example.net
Jimmy Perry - evengonzalesjames@example.org
Jesus Smith - dropvpearson@example.org
Deborah Harrington - throughoutdavisjohn@example.com
Willie Carroll - strongleslie47@example.net
Stacy Hill - Democratbhanna@example.net
Courtney Reed - southernflowersjohn@example.com
Kari Mckenzie - significantlaura99@example.com
Erin Robinson - awayafisher@example.com
Gary Cole - wouldnicholaspeterson@example.net
Edward Williams - structuresmithhannah@example.org
Jessica Garcia - unitcolekaren@example.com
Bradley Williams - boxvazquezernest@example.com
Kristie Miller - roomelizabeth88@example.com
Adam Delacruz - summerjohnmarks@example.org
Krystal Dougherty - groupshanebriggs@example.com
Bryan Morris - commonselena03@example.com
Daniel Everett - havepiercekelly@example.net
Joshua Cox - modelmyork@example.com
Erik Wagner - aftervelasquezjoseph@example.com
Justin Curry - occurkimberlycoleman@example.com
Michael Williams - restcharlotte67@example.net
Jonathan Silva - musicstonejeffery@example.org
Shane Beltran - meetrandy50@example.net
Benjamin Warren - approachjohndavis@example.net
Tanya Green - sisterzcollins@example.org
Frank Leblanc - staradamflores@example.com
Eric Hopkins - namejoshua22@example.net
Rebecca Grant - mainharrisjacob@example.org
Heather Green - assumemeghan64@example.org
Robert Hartman - yourjenniferhardy@example.org
Howard Olson - majoritypaulaarroyo@example.net
Erika Griffin - darkjoshuarojas@example.org
Jeffery Rose - anothermarywright@example.com
Anthony Duffy - foothkeller@example.com
James Graham - workersteelenina@example.com
Daniel Harmon - largezalvarado@example.net
Stacy Robertson - lightcarlduke@example.org
Matthew Hernandez - doordiana32@example.com
Patricia Henry - perlgarcia@example.org
Katrina Owen - maybejenglish@example.com
Keith Sullivan - fewcourtneyriley@example.net
Brianna Ford - preparepamela16@example.org
Andrew Ramirez - passkarlhardy@example.com
Robert Diaz - whenwilliamsjudith@example.com
Kelly Cooper - guessnicole47@example.org
Natalie Owens - churchxcollins@example.org
Natalie Burton - differentmorgansimpson@example.net
Jonathan Edwards - couldplloyd@example.net
Rebekah Sanders - industryluismorton@example.com
Tommy Hill - severalsteelebrian@example.org
Kimberly Miller - indeedhanderson@example.com
Sarah Sellers - nothingrobynvasquez@example.net
Gina Boyer - buildbryanbrittany@example.com
Cindy Marks - awaykenneth94@example.com
Eric Sheppard - forgetaaron28@example.net
Dana Gaines - warvgarza@example.org
Jillian James - economicanthonygreer@example.com
Cynthia Kent - normichaelfry@example.net
Beverly Martinez - indicategutierrezjohn@example.net
Anthony Wright - starucamacho@example.com
Alicia Adams - presidentqmassey@example.org
Jaclyn Smith - behindzimmermanemily@example.org
Scott Vazquez - restkarinajordan@example.org
John Wilson - nightchandlermadison@example.com
Jonathan Elliott - Mrdanielwright@example.org
Beth Middleton - centurymaria07@example.org
Melissa Williams - seriesheatherhall@example.org
John Owens - adddennisspencer@example.org
Michelle Hutchinson - mightsteven88@example.org
Joanne Gibson - richjudywillis@example.org
David Harris - lowmike18@example.net
Madison Powell - attackevansbrandon@example.net
Brian Thomas - overstephanie59@example.com
Darren Molina - forwardiforbes@example.net
Ralph Thomas - hospitalmendezjames@example.net
Kenneth Mcneil - knowledgeegrant@example.net
Crystal Morgan - ratherheidi05@example.com
John Kemp - considergoodmanandre@example.org
Mark Jacobson - recentlyspencerelizabeth@example.com
Jennifer Sanford - nextstacy82@example.com
Nathan Walker - frontjames88@example.org
Travis Dougherty - wheredavid50@example.org
Cathy Edwards - propertycopelandkelsey@example.com
Frank Fowler - everlopezsarah@example.net
John Abbott - soongarrettgonzalez@example.org
Stephanie Taylor - thelopezkenneth@example.com
Hannah Reed - ratealisonwilson@example.com
Jacqueline Weaver - levelbarrydonna@example.net
Darlene Shaw - citytamara01@example.org
John Romero - voicerogersmark@example.org
Elizabeth Garcia - buildjasmine89@example.net
James Boone - comparedavid04@example.com
Daniel Schaefer - challengebrett70@example.org
Chase Vega - projectopugh@example.org
Mindy Morris - lotewilson@example.org
Erica Parrish - weekderrick03@example.net
Ashley Torres - begoodmanjohn@example.org
Wyatt Carroll - feelgloria29@example.com
Russell Thompson - addbaileyorozco@example.net
Molly Young - standkaren27@example.com
Allison Fowler - recordzerickson@example.net
Ian Davis - collegelaurasanchez@example.com
Donald Phillips - althoughdavistammy@example.com
James Johnson - veryaustin66@example.com
Bonnie Hess - alonekimberlywilliams@example.com
Vanessa Brown - threethomasdavid@example.com
John Murray - researchhshea@example.net
Rachel Jimenez - consumersmithselena@example.com
Mark Callahan - tradekatherinewilson@example.org
Madison Jones - adultemily38@example.org
Marcus Walker - positiversmith@example.org
Joel James - southvayers@example.org
Cindy Salas - themselvessamantha79@example.org
Michael Campbell - fastlauren85@example.org
Amanda Snyder - tonightandreamann@example.com
Jacob Cross - sensegriffinjacqueline@example.org
David Bryant - dobrittanyclark@example.com
Angela Escobar - certainlyhebertrobert@example.com
Larry Summers - whyflucas@example.org
Katherine Thompson - earlylisa40@example.net
Frank Jones - intopagedaniel@example.com
Autumn Hicks - closemorrisdominique@example.net
Melissa Ortiz - behindmaxriley@example.org
Stephanie Miller - againstjason35@example.net
Jonathan Jones - northrussell08@example.net
William Schroeder - youcjames@example.net
Carrie Johnson - finishjarvisbrenda@example.org
Kristen Anderson - chancedonald09@example.com
Karina Roberts - jobdeborah67@example.org
James Pace - understandcolemanamy@example.org
Tristan Schultz - flydramirez@example.com
Michelle Townsend - paintingamoore@example.com
Randy Smith - startvanessahoward@example.net
Scott Mcclain - fightfgallegos@example.com
Laura Lopez - stufflbrown@example.com
William Dorsey - untiltimothy32@example.net
Ashley Bradley - centraldavid07@example.org
Lindsey Lynch - outdwells@example.org
Morgan Patel - importantmariafinley@example.org
Andrew Johnson - positivedebbie25@example.com
Elizabeth Branch - oilkstephens@example.org
Michael King - productmeredith72@example.net
Thomas Keller - hournvalentine@example.com
Tina Smith - modeldianehall@example.com
Brittany Merritt - despitejodichavez@example.org
Scott Johnson - abilityharrisjohn@example.org
Michael Brooks - recentchristopher50@example.org
Steven Thompson - questionjocelyngoodman@example.org
Hector Barnes - conditiondaniel21@example.org
Holly Freeman - rockzberry@example.com
Ronald Nguyen - fathercrose@example.net
Christopher Green - maybeshawnalucas@example.com
Brittney Rodgers - agojonathan32@example.com
Jonathan Hernandez - culturecreyes@example.org
Michelle Fry - differentwhall@example.net
Sarah Patel - ownbrownsheila@example.com
Lisa Miller - discussandrewcastro@example.net
Allison Nguyen - howstevenrobinson@example.net
Brandy Heath - alongjohnsonjeffery@example.com
Brenda Holloway - firechristiantorres@example.org
Bradley Johnson - articlewebsterkimberly@example.com
Garrett Walter - hardcmyers@example.com
Ryan Mcclain - storyzmoon@example.net
Sharon Davidson - orlbrooks@example.org
Walter Torres - lookmialucero@example.org
William Richardson - endtwalker@example.net
Christopher Fleming - stafflorimartinez@example.com
Brandi Evans - somethingmorsekathleen@example.com
Christopher Stuart - researchjulie45@example.org
Anthony Paul - onlyjessica25@example.com
Tammy Gonzales - picturebennettmelissa@example.com
Richard Rodriguez - trainingbpierce@example.net
Heidi Wheeler - conferencebalexander@example.net
Shannon Valenzuela - bookfryjessica@example.net
April Bell - nowyball@example.com
Denise Oconnell - willpkelly@example.net
Michael Copeland - concernsheliabond@example.com
Tina Rush - yourrachel53@example.org
Kelly Wong - professorduncanzachary@example.net
Karen Reyes - centralmcleanfrank@example.org
Laurie Benton - waytorresjessica@example.org
Lauren Jenkins - phonejohnstonjoyce@example.com
Alicia Dunn - theoryysingleton@example.org
Steven Banks - headvelasquezjennifer@example.com
Joseph Sanchez - machineaustinandrew@example.com
Suzanne Cummings - beginamiller@example.com
Johnathan Gomez - Democrathmartin@example.com
Angela Casey - southerncharleshorton@example.net
Marc Reyes - typejmullins@example.net
Christopher Garner - throughkarenrobbins@example.org
Justin Greer - wonderjeremy12@example.net
Dawn Mitchell - affectjohnsonalexander@example.org
Joshua Perez - internationalheatherhammond@example.com
Adam Mullen - daughtergriffinrachel@example.org
Johnathan Haas - economicwilliamhanna@example.org
Carlos Bird - preparesgarrison@example.net
Christopher Nielsen - companyjoshualucero@example.net
Michael Velez - staythomas23@example.org
Mary Mayo - paymwallace@example.net
Jared Campbell - majorityjustin64@example.net
Linda Thompson - applyaustinlawrence@example.net
Logan Petersen - actcody25@example.net
Charles Mann - himbrookstammy@example.com
Eric Reed - seriousbmayer@example.org
Matthew Wood - discoverqmitchell@example.com
Becky Jones - thiselizabeth81@example.com
John Martin - Mrsujohnson@example.net
Andrew Patterson - paybrandisanchez@example.com
Rachel Graham - suddenlymaldonadokimberly@example.org
Andrew Bradford - stylepaul49@example.com
Jeffrey Dixon - nextehendrix@example.org
Mary Barr - nationwilliamsbryan@example.org
Ruben Hill - continuestevenholmes@example.net
Vanessa Parks - orkenneth79@example.org
Albert Spence - ourksutton@example.net
Theodore Smith - throughdonnadecker@example.net
William Hamilton - stuffxcollins@example.org
Jorge Mcdowell - westernmendozaandrew@example.org
Justin Brown - yourangelicahunter@example.net
Laura Wolf - westewhite@example.com
Leah Walsh - housekathleen61@example.com
Jared Swanson - availablealexis28@example.com
Christine Williams - bluejoseph53@example.com
Lauren Johnson - soldierjoeldeleon@example.org
Jared Baker - dropphillipsedward@example.net
Devin Sims - staffericamartin@example.net
Maurice Smith - nicewatkinsnathan@example.org
Robert Graves - sixmichelle76@example.com
Amy Jackson - fatherkendra88@example.net
Jacob Stanley - boxdawnsullivan@example.com
Jason Collins - somebodysbarker@example.net
Richard Skinner - kindjillcollins@example.org
Jamie Daniels - runmeganmartinez@example.net
Patricia Salinas - rememberolarson@example.net
Mia Vaughn - southernljames@example.org
Marcus Farmer - particularbriggssean@example.net
Jeffrey Sampson - leadjonathanfriedman@example.org
Tyrone Lloyd - particularereyes@example.org
Craig Gillespie - citizenlluna@example.com
Anthony Meyers - formmmaynard@example.net
Susan Hernandez - picktoddgraves@example.org
Brenda Snyder - structureroyharris@example.org
Morgan Andrade - significantallisonhernandez@example.com
Joseph Ford - dealgpalmer@example.com
James Hernandez - similarbrittany85@example.com
Brooke Contreras - charactercourtneydurham@example.org
Michael Browning - twobenjaminflores@example.org
Leah Sanford - oldjreed@example.net
Sandy Montgomery - atilee@example.net
Anthony Dawson - gunboydchad@example.net
Nicole Jimenez - firstchristopher00@example.com
Taylor Black - somehannah98@example.org
Kelly Johnson - schoolgavin30@example.com
Kevin Johnson - taxtiffanywells@example.net
Ryan Lester - agreementasanders@example.net
Jason Crawford - interestingrodney22@example.net
Ashley Lynch - trialamyblair@example.net
Nathan Rodriguez - thanrose62@example.org
Maria Dunn - networkbelinda64@example.net
Isaac English - officialcharlesmurray@example.com
Tammy Johnson - focusmark61@example.net
Amanda Fernandez - skinkmeyer@example.com
Brian Austin - subjectlisa19@example.org
Ashley Anderson - lifemeyeramanda@example.net
Craig Brown - joinplloyd@example.com
Jason Myers - availablerodrigueztracy@example.com
Ashley Miller - musichannah86@example.com
John Flores - businessbellis@example.net
Nicole Lee - countryluis16@example.org
Cristian Wright - radioandersontravis@example.net
Keith Johnson - partyjon48@example.net
Luis Moore - whiteariana82@example.net
Jeffrey Taylor - PMamarquez@example.org
Susan Oneill - monthkimberly95@example.net
Katelyn Reed - Istewartjoe@example.com
Karina Johnson - lawmoralesmatthew@example.org
David Richmond - althoughvillaamy@example.org
Kathryn Short - paymakaylathomas@example.com
Cody Mcdonald - situationrebecca39@example.com
Joseph Jackson - hourtashapierce@example.net
Shannon Brown - controlann33@example.net
Aaron Benjamin - pricecswanson@example.com
Alyssa Griffin - sometimesmward@example.org
Alfred King - gardenjonathanreynolds@example.com
Tina Davis - musicrobert33@example.net
Carlos Leonard - thankallenroy@example.com
Larry Crawford - publichallbrandon@example.net
Mike Nichols - severaluoconnell@example.com
Angela Brown - eachdenise34@example.net
Deborah Turner - readcody46@example.net
Angela Franklin - townperezmichele@example.org
Andrew Cordova - quicklyalex93@example.com
Dennis Benton - outsideqspence@example.org
Sarah Hall - againstdonaldali@example.org
Monica Pearson - crimebonillajennifer@example.org
Melissa Stone - edgewchristian@example.org
Jessica Williams - storejdaugherty@example.org
James Morgan - bestcolephillip@example.org
Jason Brown - medicalahudson@example.net
Natasha Maldonado - worryocabrera@example.org
Crystal Hodge - countrybmoore@example.net
Michelle Franklin - structureyduncan@example.net
Lisa Vasquez - coversabrina79@example.org
Joseph Griffin - muchbrownangela@example.net
Pamela Adkins - gunjesus10@example.org
Shannon Stone - soundethomas@example.com
Claire Morgan - clearsergioprice@example.com
Jennifer Bennett - casemartinmichael@example.org
Sydney Perez - theredanielmoyer@example.net
Nicholas Lowe - samereginald27@example.net
Timothy Bowman - joinlisa42@example.com
Isaiah Zavala - wantkellyreid@example.net
Jordan Garrett - strongbrandon78@example.net
Aaron Kent - senseloganjohn@example.org
Zachary Rodriguez - pushthomassmith@example.com
Donald Williams - tooysanchez@example.org
Rodney Ross - strategyevelyn70@example.org
Mary Boyd - ballkmartin@example.org
Alejandro Rivers - policeashley02@example.net
Bridget Foster - pricedavid42@example.org
Cindy Wolfe - peacepvalencia@example.com
Jamie Hughes - careerrodriguezamy@example.net
Molly Mendoza - sendbishopfaith@example.net
Nancy Johnson - createwebbmichael@example.org
Gwendolyn Prince - twokaren20@example.net
Rebecca Owens - almostgabriel07@example.com
Jennifer Burgess - movementljoyce@example.org
Amber Lane - seriesmelinda72@example.net
Eduardo Gomez - norbrookerichardson@example.net
Vincent Harper - specificamber49@example.com
Christopher Parker - religiouserikaholloway@example.net
Christy Bishop - medicalnhall@example.com
Tiffany Hicks - betweenchristopher79@example.org
Gene Collins - butdnguyen@example.com
David Richardson - spendjessicagrimes@example.net
Jonathan Hayes - riskmelissamontgomery@example.org
Michael Burns - concernandrew15@example.org
Jamie Pearson - regionperezchristian@example.org
Shawn Johnson - abilitytanyarodriguez@example.org
Connie Harper - makevnewton@example.net
Robin Horn - showjennifer27@example.com
Brianna Long - motherbrandonperry@example.org
Jessica Miller - wifechristinaparker@example.net
Sean Gray - lighthollywarren@example.org
Harold Pollard - throughouttorresarthur@example.net
Jonathon Sanders - latejoseph27@example.org
Christopher Jackson - prettybcraig@example.com
Rachel Barajas - spacelewiscarolyn@example.com
Craig Hill - girlmooreamanda@example.net
Melinda Frey - jobtiffany38@example.net
Sharon Davis - cellsmithwilliam@example.org
Jennifer Taylor - stagekellygarrett@example.com
Madeline White - politicsdaniel46@example.com
Heidi Jones - astravisstewart@example.org
Angelica Hurst - dealmichael04@example.org
Russell Nguyen - describepatricia78@example.net
Corey Blackwell - agobecky22@example.org
Natasha Johnson - caselisamitchell@example.com
Shannon Durham - avoidfrances38@example.org
Michael Martinez - okjasonjohnson@example.org
Andrew Hardy - pieceginawhite@example.com
Michele Duncan - gardendeckerchristina@example.net
Diane Mata - paperjhill@example.com
Samantha Hawkins - somematthew22@example.org
Donna Odonnell - flylaura15@example.com
Danielle Wood - enjoythomasgarner@example.com
Nicholas Lopez - attorneybrittanyjones@example.com
Stephanie Castro - wondermelissa45@example.net
Matthew Brown - sourcepdickerson@example.org
Cameron Tucker - structurejason91@example.org
Jennifer Edwards - followchristopher81@example.net
Brittany Riggs - todaypterry@example.com
Timothy Rodgers - imaginemackbrandon@example.com
Daniel Sullivan - anyppayne@example.net
Regina Burke - actuallyjason80@example.com
Tiffany Miller - investmentbrownchristopher@example.org
Daniel Garcia - returntatemarvin@example.org
Dave Brown - challengejakehayes@example.org
Kelly Barnett - darkgraceramirez@example.org
Stephanie Nelson - attackhickmankristy@example.com
Jeffrey Villanueva - restjessicahendricks@example.com
Kristina Freeman - beginsmithmichelle@example.org
Kenneth Espinoza - officercindyreyes@example.com
Amanda Joyce - racemadisonjames@example.org
Angela Shaw - weekohumphrey@example.com
Mary Turner - careerrandy86@example.net
James Long - norwnewman@example.org
Ethan Williams - lotdavid74@example.net
Louis King - carcraig55@example.net
Leah Walker - identifysmithanthony@example.net
Jodi Young - byochoaamber@example.net
Nicole Melton - policekingrobyn@example.org
Stephen Reese - studyquinnnoah@example.com
James Allen - respondgaryriley@example.org
Mary Crosby - readqwalker@example.net
Eric Cortez - oilbenjamindickerson@example.org
Lori Ramirez - existudavis@example.net
Charles Wells - powerlarry50@example.org
Andrew Compton - energyrcrosby@example.com
Katelyn Perez - agentkayla43@example.org
George Cantu - calldsmith@example.com
Christina Prince - fullwilliamleon@example.net
Dennis Johnson - legdana11@example.com
Lindsay Escobar - reddebrawatkins@example.net
Joshua Cook - followchelsea20@example.org
Ronald Hess - provekeithboyd@example.org
Brianna Cox - remainjoel54@example.net
Thomas Short - eightswilliams@example.com
Stuart Moore - whognorton@example.com
David Thomas - memorychristophercampbell@example.org
Brandon Lopez - paintingalicia16@example.com
Chelsea Cox - thoughdavidhorne@example.com
Christina Griffin - beginannacarpenter@example.net
Ellen Lee - oildyoung@example.net
Kathleen Macdonald - firstmartinmatthew@example.org
Jessica Walls - preparekenneth39@example.net
Robert Peters - lossbriggscrystal@example.org
Billy Rogers - onblake06@example.com
Kelly Reeves - classalexander65@example.com
Wesley Ayers - aroundjohn30@example.org
Valerie Long - patternhaley21@example.org
Jean Chase - mediaschwartzmichelle@example.com
Joshua Oneill - numberwhitney18@example.com
Philip Hughes - mouthqmartinez@example.com
Christina Harrington - nearifisher@example.com
Jessica Walls - establishswilliams@example.com
Glenn Harris - hekwhite@example.org
Todd Hopkins - mindshaun57@example.com
Lori Bennett - performgregory58@example.org
Crystal Armstrong - stuffblackburnsabrina@example.com
Christian Fry - thoughtjonathancarr@example.net
Dustin Johns - coldadam16@example.com
Joseph Perez - seatbeckybarnett@example.com
Teresa Miranda - waittimothy81@example.com
Sandra Lee - nocampbelljohn@example.org
Eric Stevenson - commercialcheryl05@example.net
Susan Alvarez - footcynthiaallen@example.net
Michael Henderson - alsodebraavila@example.com
Travis Chapman - thirdtoni76@example.net
Diane Ward - structurejrodriguez@example.net
Robert Davidson - rightalvarezthomas@example.com
Jose Lambert - voterrivas@example.com
Emily Hart - pagekatherine29@example.com
Barbara Wallace - hairmoranluis@example.com
Rachael Duncan - cardgregdavis@example.net
Kimberly Gibson - pagecheryl38@example.com
Kenneth Hart - whomjoseph81@example.com
Jason Howell - policyandradechristopher@example.net
Jason Parks - secondrobinsonvictor@example.com
Rachael Johnson - viewdonaldsonscott@example.org
Joan Crane - firsttinareid@example.net
Karen Perry - realmichele64@example.net
Kirsten Woods - Democratrichardgarcia@example.org
Deborah Gregory - informationihansen@example.com
Richard Brown - takerobertyoung@example.com
Joseph Conner - safepagekendra@example.org
Elizabeth Carson - meandavidanderson@example.org
Carlos Sanders - letclarkamanda@example.net
Maria Morgan - selltommy64@example.net
Sandra Harrington - machinepetersendavid@example.org
Morgan Alvarez - schooltanya26@example.org
Kenneth Schwartz - himrobert65@example.org
Emily Miles - longcarl40@example.net
Eric Mcbride - whilecatherinefoster@example.com
Anthony Shaw - actuallybellis@example.com
William Kline - verycaitlin04@example.com
Kyle Hill - wonderaalexander@example.net
Jerry Kemp - thoughtzhoward@example.net
Karen Paul - leveljohnsondavid@example.org
Amber Glover - roleycordova@example.net
Brandon Lee - describekaren78@example.net
Joseph Jones - carryhudsonjeremiah@example.com
Kim Hays - protectjamesgill@example.org
Jessica White - dataqjackson@example.org
Johnny Bradley - politicsangela12@example.net
Rebecca Campbell - fastccalderon@example.net
Brent Miller - everythingmelissasilva@example.org
Veronica Stephens - reasonmorenobryan@example.net
Taylor Solomon - certainlyjimenezjames@example.net
Kristina Taylor - heavyufleming@example.com
Amber Warner - qualitykatie72@example.org
Dustin Norris - powerbrent61@example.net
Amy Case - benefitkylie55@example.org
Courtney Campbell - throwpatriciadaugherty@example.org
James Rose - daughterdustin94@example.net
Daniel Harris - quicklyvreyes@example.net
Ashley Miller - followjerry33@example.com
Karen Hill - fillpmiller@example.net
Donald Zhang - servemarylewis@example.net
Michelle Nguyen - itselfrrodriguez@example.com
Kristen Logan - carejohnsonandrew@example.org
Joshua Taylor - collectiondaniel02@example.org
Mary Cortez - lastccarroll@example.com
Angela Davidson - knowledgedaltonstephanie@example.net
Angela Roberts - itsbrandondavis@example.org
Christine Cuevas - sectionmartinezstanley@example.com
Linda Webster - perphillipsjennifer@example.com
Deborah Barrett - forceoyoung@example.net
Brandon Mcknight - eventheresa60@example.org
Gregory Johns - weightchristopher58@example.com
Linda Young - themfdawson@example.com
Anna Flores - identifyjhill@example.org
Jamie Christensen - measurewalter33@example.com
Daniel Graham - putzstone@example.com
James Gray - technologyemily35@example.org
Melissa Jones - recentlyegentry@example.com
Robert Brooks - playermfernandez@example.org
Rodney Stewart - numberelizabethgraves@example.com
Janet Miranda - throwemily03@example.net
Wanda Jimenez - meetingcfletcher@example.net
Kaitlyn Russell - oiljennifer95@example.net
Stephanie Smith - computermcfarlandyvonne@example.org
Alison Davis - showkathleen99@example.net
Mary Hernandez - bigjohnsonbrent@example.org
Raven Smith - costashley43@example.com
Joshua Tucker - itselfgwilliams@example.net
Lisa Russell - tengutierrezkristina@example.net
Kimberly Ramsey - lightrobert27@example.org
Wendy Taylor - theyamcfarland@example.com
Jasmine Blankenship - bigtoni79@example.net
Sarah Weaver - downrubenevans@example.org
Catherine Houston - goalamartinez@example.net
Angela Ayers - thoughtakramer@example.org
Pamela Murphy - knowledgebowmanjonathan@example.org
Brian Walker - remainnleach@example.net
Charles Turner - eveningepotts@example.com
Heidi Harris - threattaylorapril@example.org
Clayton Torres - freemelinda39@example.com
Robert Holmes - specialharrisjamie@example.com
Rachel Goodwin - fourbflores@example.net
Patrick Frederick - mainbrittney33@example.org
Eddie Jones - dinnerlisa39@example.net
Chloe Thompson - thoughtmurphybill@example.com
Andrea Adams - suddenlyjosborne@example.org
Jacob Decker - withoutcgrant@example.org
John Page - approacheringalvan@example.com
Monica French - howeveramanda75@example.org
Kelly Hardy - leastgarciaryan@example.net
Ronald Casey - agestevenjones@example.com
Amber Diaz - thesegonzalezeric@example.net
Shaun Wilson - niceheather67@example.com
April Cervantes - seabutlerlaura@example.net
Samantha Molina - grouphlewis@example.com
David Simmons - tellchristophershah@example.org
William Ramos - lossayersjoyce@example.com
Elizabeth Lewis - ourneilgeorge@example.net
Adrian Chavez - sitefernandezjames@example.org
Justin Anderson - lifedawn60@example.com
Penny Castro - leadcarrie76@example.net
Denise Hall - thosejohnreyes@example.org
Michael Robinson - describemunozcharles@example.com
Wayne Collier - accordingdillonbennett@example.org
Joseph Fuentes - continuehenryibarra@example.org
Kimberly Swanson - consideredwardgarcia@example.org
Keith Bailey - reportharrisonjessica@example.com
Peter Johnson - oktinawhite@example.net
Stephen Scott - smalljeanramsey@example.com
Tina Welch - optionbuchanansarah@example.net
Matthew Edwards - whodmorton@example.org
April Mathews - crimejgoodwin@example.com
Scott Rodriguez - involvetina37@example.net
Jacob Webster - togetherpaulshea@example.net
Walter Costa - fastcaitlin38@example.org
Mike Martinez - federalehamilton@example.net
Tom Gibson - languagekimberly17@example.org
Derek Grant - develophaneymichael@example.org
Amy Morgan - morelcole@example.com
Laura Harmon - bothnicholasross@example.com
Zoe Ferguson - controllisahouse@example.com
Margaret Sawyer - viewjoseph07@example.org
Susan Green - smallsarahrichards@example.com
Deborah Williams - owntravis68@example.net
Charlotte Pruitt - foreignjohnsonclifford@example.org
Jamie Ramirez - catchjohnsonelizabeth@example.org
Kirsten Mitchell - balllaura93@example.com
Michael Owens - socialamy37@example.org
Melinda Smith - indicatencooper@example.com
Sherry Combs - whilelreeves@example.net
Jake Sanders - partmartinezdrew@example.com
Tanner Flores - includingamanda70@example.com
Edward Wright - hearreneesanchez@example.net
David Thomas - answerdaniellesmith@example.com
Chase Lopez - wellsarahpeterson@example.net
Tiffany Daugherty - accordingbryantedwin@example.org
Laura Holden - styletaylorking@example.org
Elizabeth Smith - useplee@example.net
Anna Henry - personalbowerstheodore@example.com
Timothy Roberts - ratedarrellmarshall@example.net
Alexander Sanchez - militarysaraboone@example.com
Matthew Morrison - situationfitzgeraldtammy@example.com
Corey Santos - ablergreene@example.com
David Johnson - throwmillerashley@example.com
Vincent Patterson - articlejuangillespie@example.net
Jeffrey Jackson - footmorserichard@example.org
Angela Fox - uscmack@example.org
Henry Smith - scienceleebrittany@example.net
Jonathan Miller - sonryanwright@example.org
David Pearson - dealmichaelcrosby@example.org
Richard Barajas - frontkhall@example.org
Tina Clarke - fearwoodkelly@example.net
Carl Ferrell - nightzperez@example.com
Charles Ramos - votesuzannelogan@example.net
Derrick Smith - boardkimberly21@example.net
Colin Lane - pullelliottedward@example.com
Michael Villa - somethingwolfadam@example.org
Luis Black - laughsusan37@example.org
Brandi Robinson - believejohn85@example.org
Monique Perry - blacklonnieingram@example.net
Robert Palmer - medicalgoodfrancisco@example.org
Jennifer Wilson - losemooneyrichard@example.net
Eric Green - dealggarcia@example.org
Robert Brooks - personcindy64@example.com
Karen Meyer - votebairdamy@example.org
Julia Olson - ourcarlos23@example.org
Melody Norris - manqstewart@example.com
Bryan Nelson - enternwalker@example.org
Chris Myers - evenaaronlucero@example.com
Devon Ayala - officialtoni77@example.com
Kelly King - peoplelcampbell@example.com
Jonathan Hartman - arguekelly77@example.com
Christopher Wallace - passmeredith89@example.net
Victor Kelly - memorymadisonmoore@example.com
Robert Rodriguez - costmartin81@example.org
Victoria Bush - thoseyorkemily@example.org
Mary Hanson - knowledgejohnslisa@example.net
Brittany Mcfarland - internationaluporter@example.net
Paul Wallace - wondershane58@example.com
Sarah Acevedo - forwardcaldwellcrystal@example.org
Susan Bauer - magazinetmason@example.org
Carolyn Durham - seasonchristopherroman@example.com
Bobby Tyler - rangerandy81@example.org
Erica Yu - middleandrewwilliams@example.org
Laura Sims - everythingrperry@example.net
Jessica Perez - thanbradleyjohnson@example.net
Katherine Lowe - gocarlsonmelinda@example.net
Jacob Baldwin - alreadyrachel18@example.com
Jason Bartlett - personalvanderson@example.com
Elizabeth Kline - becauseanthony54@example.com
Dillon Brown - readyxmorales@example.com
James Lopez - imagewaltersnathan@example.org
Deborah Richmond - newyjackson@example.com
Patricia Walker - partmillergina@example.org
Joyce Olson - personalbrian97@example.org
Lisa Jefferson - goortegagary@example.net
Sara Lyons - peopledominguezjustin@example.org
Debra Jackson - unittrosales@example.org
Samantha Riley - groupdorismorgan@example.net
John Kim - setxmeadows@example.net
David Neal - anyvictorjordan@example.org
Jessica Rodriguez - appearmegan97@example.net
Megan Carter - governmentmichael26@example.com
Adriana Moore - spacewhicks@example.org
Donna Wilson - testohenderson@example.org
Stephen Mendoza - bettertaylorjesse@example.net
Anna Lawson - dogdavidleon@example.org
Eric Rodriguez - workshannonbrenda@example.net
Terri Poole - boxdanielle22@example.com
Gina Johnson - livewdalton@example.org
Trevor Clements - technologyruizkrista@example.org
Michael Washington - piecewilliamcurtis@example.org
Jonathan Jones - concernblakehenry@example.org
Deborah Wilson - nicediazrandy@example.net
Melissa Smith - paintingcampbelltony@example.org
Erika Nguyen - tonightboothjillian@example.com
David Wagner - spendjennifer21@example.net
Amanda Miller - anyonewallmark@example.org
Robert Walker - purposewoodjamie@example.org
Teresa Park - remaincherylgonzalez@example.org
Juan Anderson - childrobertbates@example.net
Sandra Lowe - theygeorgediana@example.com
Michael Kelly - defenseymills@example.org
Danny Gross - assumedanielleglover@example.com
Timothy Allen - anythingkelleyjessica@example.com
Samantha Butler - throwssutton@example.net
Matthew Crawford - agencydavisdarrell@example.com
Rebecca Snyder - historyanthonyhughes@example.com
Tammy Ramirez - listtrobinson@example.org
Karen Paul - soowilson@example.net
Stacy Jones - thinkjerry56@example.com
Heather Hicks - prettyandrewweaver@example.net
Savannah Ford - truemccoyrichard@example.net
Evan Riley - talkjonestammy@example.org
Raymond Johnson - watchnhale@example.com
Hannah Freeman - suggesthuntandrea@example.net
Marc Wright - federalybond@example.net
Brent Harris - preparealvareztammy@example.com
David Thompson - himselfgrantkimberly@example.com
Jennifer Price - wholedanieljones@example.org
Harold Wagner - nearlyahenry@example.org
Amanda Perry - ifwgarcia@example.org
Linda Owens - eitherangela42@example.com
Gary Martin - futurerichardsonerica@example.net
Billy Valentine - arrivelongvanessa@example.com
Janet Wright - sameashleysims@example.net
Ryan Olson - jointheresatucker@example.net
Mark Cox - projectbarbararusso@example.org
Samuel Martin - whitejennifer35@example.com
Matthew Pennington - establishjenniferpitts@example.org
Emily Brooks - applykarenkim@example.org
Stephen Anderson - amountjohnsonstacy@example.net
Joyce Obrien - namesara27@example.org
Marissa Howell - restjustin54@example.org
Sheila Todd - sorttedwards@example.com
Erik Flores - towardscotttracy@example.com
David Casey - regiondickersonpamela@example.org
Donald Wright - particularkgarcia@example.org
Mason Garcia - northgreid@example.org
Robert Gonzalez - fourjasminemiller@example.com
Brandy Richards - commercialmatthewsbrian@example.org
Jillian Lowery - childjamespearson@example.org
Joan Johnson - containkelleyjohn@example.com
Katherine Richardson - Ibfields@example.net
Leah Marsh - listenrandy46@example.org
Patrick Wallace - simplehanderson@example.com
Jonathan Wilson - particularlymelindafreeman@example.net
Kendra Miller - throughterritran@example.org
Brenda Jones - wholeshanefuller@example.org
Nicole White - normonica92@example.org
Andrea Rivera - indeedorozcodavid@example.net
Mitchell Daniel - staffrobert27@example.net
Cheryl Weeks - designkristen15@example.org
Blake Zhang - pastmichaelacosta@example.org
Cory Mccann - protectwthomas@example.com
Elizabeth Harrington - allowdylanstevens@example.net
James Richardson - differentiwoods@example.net
Rhonda Chambers - visitgene45@example.net
Michael Miller - effectchristinajenkins@example.net
Megan Nguyen - industryobarnes@example.org
Amber Wood - treeisandoval@example.com
Paul Soto - simplyjeffrey23@example.org
Jonathan Knapp - significantyesenia61@example.net
Mark Brown - sellmartinnicole@example.org
Kara Jones - particularchristophermcintyre@example.org
Taylor Jones - asharrissusan@example.net
Luke Duarte - windobrown@example.net
Stephen Washington - willdwilliams@example.net
Daniel Howell - audienceshawn63@example.net
John Ross - downawade@example.org
Bryan Davis - easygarzasteven@example.net
Heidi Young - finemelissasuarez@example.com
Chad Werner - meanhowelltyrone@example.com
Tonya Chase - conferenceronald45@example.com
Dustin Ramirez - trialogamble@example.org
Randy Johnson - merodriguezlisa@example.com
Aaron Morales - institutionlaurenallison@example.net
Frances Ward - allsean74@example.net
Matthew Kane - healthmcdanieldestiny@example.org
Alexis Smith - forceandrew38@example.org
Tyler Richard - summerangela63@example.net
Daniel Carroll - beyondraymondtaylor@example.com
Kara Johnson - thankwatsondevon@example.net
Linda Davis - authorsimpsonkathleen@example.net
Justin Edwards - othersjosephbennett@example.com
Aimee Edwards - almostkelli67@example.org
Jennifer Gomez - healyssalewis@example.org
Vincent Griffin - monthgarrettbutler@example.net
Jonathan Ross - aroundshieldsthomas@example.org
Karen Rose - keybenjamin93@example.org
John Stanley - considermserrano@example.net
Laura Stark - musiciglass@example.net
William Diaz - studyobecker@example.org
Nicholas Jones - entirecandicejohnson@example.com
William Caldwell - easyjoannafry@example.net
Bruce Smith - naturejmoore@example.com
William Mendoza - whosejerrymoreno@example.net
Jeanne Stout - policyfclarke@example.org
Daniel Bishop - areasusanrobinson@example.com
Lindsey Conrad - acceptegarcia@example.org
Susan Schwartz - productstevenlarsen@example.com
Gary Hurst - riskholmesjennifer@example.com
Maurice Blair - whilehernandeztanya@example.net
Gary Evans - prettybeth86@example.org
Meagan Green - officervanessa94@example.org
Charlene Colon - movementthomassnyder@example.net
Christine Cooper - treatnelsonfrederick@example.net
Savannah King - ableowood@example.com
Victoria Washington - culturalgabrielsmith@example.net
Yolanda Phillips - thesewoodwardsusan@example.net
Matthew Frederick - happyruizdonald@example.net

### Числовые сравнения
3. Найди все книги, цена которых меньше 500.  
In [10]: from books.models import Book
In [11]: list_books = Book.objects.filter(price__lt=500)
In [17]: list_books
Out[17]: <QuerySet []>
 
4. Найди все книги с ценой не более 300.  
In [18]: list_books = Book.objects.filter(price__lte=300)
In [19]: list_books
Out[19]: <QuerySet []>

5. Найди все книги дороже 1000.
In [22]: list_books = Book.objects.filter(price__gt=1000)[:100]
In [23]: for b in list_books:
    ...:     print(b)
    ...: 
Meeting letter mean., Angela Escobar - certainlyhebertrobert@example.com : 2023-02-22 00:37:31.716172+00:00, 3344.98, 312.02, {'genre': 'affect', 'pages': 148}
Professional keep., Victor Kelly - memorymadisonmoore@example.com : 2020-06-28 22:49:55.351064+00:00, 1295.24, 395.76, {'genre': 'player', 'pages': 132}
Meeting environment., Donald Zhang - servemarylewis@example.net : 2023-06-16 10:05:45.086483+00:00, 1168.09, 357.66, {'genre': 'from', 'pages': 131}
New third story., Eric Lee - winclarkdeanna@example.com : 2022-02-07 14:12:54.952720+00:00, 3276.58, 372.19, {'genre': 'data', 'pages': 217}
Exist executive., William Richardson - endtwalker@example.net : 2020-03-22 04:05:09.242319+00:00, 4121.63, 251.97, {'genre': 'soldier', 'pages': 262}
Fear., Brandon Mcknight - eventheresa60@example.org : 2023-11-25 02:28:17.794569+00:00, 2339.26, 88.25, {'genre': 'writer', 'pages': 490}
Beyond respond consider., Harold Wagner - nearlyahenry@example.org : 2024-02-24 20:06:18.649125+00:00, 4567.98, 334.74, {'genre': 'unit', 'pages': 468}
Explain store general., Corey Blackwell - agobecky22@example.org : 2021-05-18 14:19:34.280770+00:00, 4397.39, 184.80, {'genre': 'under', 'pages': 195}
Painting decide., Erin Robinson - awayafisher@example.com : 2021-01-13 05:48:47.603779+00:00, 2834.37, 227.06, {'genre': 'though', 'pages': 148}
To seem live., Kelly Wong - professorduncanzachary@example.net : 2025-06-15 18:10:38.601416+00:00, 3554.58, 289.80, {'genre': 'opportunity', 'pages': 451}
Fact very., Billy Valentine - arrivelongvanessa@example.com : 2020-09-01 20:10:07.733161+00:00, 1900.60, 56.77, {'genre': 'middle', 'pages': 460}
Low., Eric Green - dealggarcia@example.org : 2020-09-08 19:34:08.540429+00:00, 2600.32, 437.09, {'genre': 'best', 'pages': 344}
Sing., Stephanie Castro - wondermelissa45@example.net : 2021-01-27 23:32:18.693934+00:00, 3792.01, 20.85, {'genre': 'defense', 'pages': 137}
Personal., Kelly Hardy - leastgarciaryan@example.net : 2020-06-14 21:58:05.944401+00:00, 4295.98, 161.00, {'genre': 'store', 'pages': 340}
Instead thank., Nicole Jimenez - firstchristopher00@example.com : 2023-08-26 03:21:51.787934+00:00, 3845.65, 341.32, {'genre': 'popular', 'pages': 174}
Industry large., John Romero - voicerogersmark@example.org : 2020-03-02 08:03:39.600936+00:00, 1526.15, 67.95, {'genre': 'agreement', 'pages': 232}
Adult once lead., Eric Stevenson - commercialcheryl05@example.net : 2022-01-29 12:48:04.840868+00:00, 4797.42, 135.98, {'genre': 'sport', 'pages': 108}
Political fire., Carlos Bird - preparesgarrison@example.net : 2020-10-23 10:09:45.968190+00:00, 3244.97, 289.99, {'genre': 'exactly', 'pages': 493}
Travel college condition., Brittany Harding - explainlisa82@example.org : 2022-11-28 08:49:14.605953+00:00, 3732.66, 359.33, {'genre': 'range', 'pages': 446}
Step accept senior., Angela Ayers - thoughtakramer@example.org : 2021-09-22 08:32:39.470432+00:00, 3287.96, 175.65, {'genre': 'prove', 'pages': 406}
We current popular., Michele Williamson - strongjosephjones@example.org : 2024-08-25 13:31:12.192678+00:00, 3798.76, 407.86, {'genre': 'second', 'pages': 267}
Shake take law., Brittany Mcfarland - internationaluporter@example.net : 2021-12-24 07:11:00.353744+00:00, 4098.23, 60.53, {'genre': 'police', 'pages': 218}
Ask TV., Christopher Rogers - billamberjones@example.com : 2024-10-10 20:23:04.896218+00:00, 2844.66, 320.46, {'genre': 'near', 'pages': 451}
Sort morning., Savannah King - ableowood@example.com : 2020-01-02 01:29:47.573082+00:00, 4190.75, 67.15, {'genre': 'that', 'pages': 142}
Your value., Margaret Pena - purposebridgetdavis@example.org : 2025-04-06 06:03:55.901639+00:00, 4257.08, 2.16, {'genre': 'reality', 'pages': 204}
Television business., Gary Martin - futurerichardsonerica@example.net : 2020-02-12 17:17:38.004358+00:00, 3446.25, 436.92, {'genre': 'contain', 'pages': 155}
One office against., Luke Duarte - windobrown@example.net : 2020-01-27 00:04:59.042336+00:00, 3002.12, 441.30, {'genre': 'where', 'pages': 332}
Example behind., Kristina Taylor - heavyufleming@example.com : 2021-07-01 19:39:06.748351+00:00, 4478.69, 366.30, {'genre': 'firm', 'pages': 150}
Move hand., Karen Reyes - centralmcleanfrank@example.org : 2022-10-26 10:12:40.893220+00:00, 3578.45, 11.17, {'genre': 'even', 'pages': 299}
Professional fall peace., John Kane - bodyjohnsonalexandria@example.net : 2022-10-22 04:45:37.603637+00:00, 2812.32, 136.52, {'genre': 'window', 'pages': 400}
Fire suffer around radio., Chad Dunn - investmenturamos@example.net : 2024-09-15 19:47:58.925880+00:00, 2818.96, 375.67, {'genre': 'mother', 'pages': 259}
Season start., Robert Graves - sixmichelle76@example.com : 2024-09-13 06:46:21.382140+00:00, 1403.68, 430.87, {'genre': 'kitchen', 'pages': 164}
Total usually., Jorge Mcdowell - westernmendozaandrew@example.org : 2022-05-05 01:59:54.107788+00:00, 1397.07, 422.65, {'genre': 'site', 'pages': 180}
Cut hotel., Jonathan Elliott - Mrdanielwright@example.org : 2021-06-11 04:59:18.930929+00:00, 1464.49, 243.78, {'genre': 'yourself', 'pages': 366}
Perform., Andrea Arnold - cityrhill@example.org : 2023-02-04 02:14:07.528152+00:00, 1222.16, 133.04, {'genre': 'reality', 'pages': 395}
Next top., Brianna Long - motherbrandonperry@example.org : 2022-10-03 06:39:37.601050+00:00, 2992.80, 286.05, {'genre': 'impact', 'pages': 170}
Pressure., Colleen Roberts - sourcecarlsonchristopher@example.com : 2021-11-05 14:47:56.033042+00:00, 1555.03, 42.70, {'genre': 'either', 'pages': 498}
Dog something., Brittany Harding - explainlisa82@example.org : 2025-01-07 01:15:50.357448+00:00, 3630.33, 259.81, {'genre': 'little', 'pages': 285}
Season interest., Lauren Jenkins - phonejohnstonjoyce@example.com : 2022-01-17 06:51:45.909125+00:00, 3088.07, 149.07, {'genre': 'finish', 'pages': 330}
Here choose worker., Sheila Todd - sorttedwards@example.com : 2020-12-20 21:12:45.102972+00:00, 2517.95, 216.62, {'genre': 'player', 'pages': 306}
Kitchen material lose., Denise Hall - thosejohnreyes@example.org : 2024-08-20 15:11:40.577817+00:00, 4226.24, 431.06, {'genre': 'reality', 'pages': 311}
Source probably check., Paul Webster - whilepalmersierra@example.com : 2022-01-26 20:40:47.079689+00:00, 4384.55, 225.88, {'genre': 'plan', 'pages': 224}
Sell where., Edward Williams - structuresmithhannah@example.org : 2023-01-05 23:43:20.531107+00:00, 2834.86, 422.92, {'genre': 'culture', 'pages': 148}
Forget picture yard., Robert Holmes - specialharrisjamie@example.com : 2023-01-12 10:16:55.217300+00:00, 3675.25, 258.50, {'genre': 'interesting', 'pages': 281}
Author try charge., John Smith - statementjackhardy@example.org : 2024-01-17 17:29:27.206612+00:00, 4769.70, 370.92, {'genre': 'it', 'pages': 293}
Account cover pick., Sarah Hall - againstdonaldali@example.org : 2025-04-19 15:50:15.471072+00:00, 3791.59, 107.01, {'genre': 'follow', 'pages': 345}
Experience I democratic., Jonathan Silva - musicstonejeffery@example.org : 2024-11-16 16:20:22.888509+00:00, 4584.24, 370.41, {'genre': 'hand', 'pages': 449}
Participant environmental., Natalie Owens - churchxcollins@example.org : 2024-12-20 07:04:17.914972+00:00, 3940.56, 106.55, {'genre': 'after', 'pages': 392}
Must while., Curtis Lowe - takecarla41@example.com : 2022-03-29 20:18:22.550889+00:00, 1658.50, 324.76, {'genre': 'bit', 'pages': 159}
Bad read north., Matthew Kane - healthmcdanieldestiny@example.org : 2023-07-29 18:32:56.732831+00:00, 1393.40, 372.70, {'genre': 'able', 'pages': 149}
Small bill those., Michael Burns - concernandrew15@example.org : 2020-12-26 14:01:29.142240+00:00, 3429.56, 194.65, {'genre': 'statement', 'pages': 266}
Throw., Christina Gutierrez - bagshane45@example.com : 2021-04-19 08:24:02.343942+00:00, 1466.72, 13.91, {'genre': 'citizen', 'pages': 131}
A discover machine., Robert Davidson - rightalvarezthomas@example.com : 2020-03-24 01:39:39.334835+00:00, 3597.67, 165.66, {'genre': 'provide', 'pages': 374}
Marriage series forward., Andre Ellison - betterpshaffer@example.org : 2024-02-26 02:23:30.642237+00:00, 4508.86, 342.63, {'genre': 'sure', 'pages': 399}
Drug research., Andrew Johnson - positivedebbie25@example.com : 2022-05-16 15:03:34.632036+00:00, 2150.72, 442.39, {'genre': 'stage', 'pages': 260}
Protect how., Katherine Lowe - gocarlsonmelinda@example.net : 2021-11-21 10:59:30.226649+00:00, 3226.22, 419.83, {'genre': 'woman', 'pages': 473}
Popular represent run., Melissa Williams - seriesheatherhall@example.org : 2020-05-29 06:14:42.868814+00:00, 4133.13, 207.05, {'genre': 'marriage', 'pages': 190}
Direction writer., Danny Gross - assumedanielleglover@example.com : 2022-07-09 00:40:36.570508+00:00, 2545.37, 246.02, {'genre': 'avoid', 'pages': 225}
Will bring almost., Jillian Lowery - childjamespearson@example.org : 2025-03-04 11:24:32.116129+00:00, 3768.92, 54.12, {'genre': 'design', 'pages': 257}
Enjoy I morning., Christopher Green - maybeshawnalucas@example.com : 2024-01-21 06:07:28.472442+00:00, 1012.44, 38.99, {'genre': 'month', 'pages': 174}
Ever notice up., Joanna Morris - himselfrobertwalker@example.com : 2021-08-30 19:19:48.673305+00:00, 4338.19, 280.40, {'genre': 'country', 'pages': 280}
Picture use teacher., Stephen Washington - willdwilliams@example.net : 2020-07-12 08:54:13.334060+00:00, 3284.38, 213.85, {'genre': 'reason', 'pages': 198}
Worry conference., Daniel Stone - magazinebenjaminsaunders@example.com : 2023-04-20 15:10:52.078236+00:00, 1284.96, 286.58, {'genre': 'drive', 'pages': 329}
Outside apply., Ashley Bradley - centraldavid07@example.org : 2022-08-26 17:50:10.019188+00:00, 4871.05, 40.89, {'genre': 'effort', 'pages': 491}
Start finish kitchen., Tiffany Miller - investmentbrownchristopher@example.org : 2022-03-07 18:14:21.447129+00:00, 4643.13, 31.64, {'genre': 'radio', 'pages': 200}
Pm artist season., Ashley Torres - begoodmanjohn@example.org : 2024-07-21 03:42:51.277729+00:00, 4234.48, 209.09, {'genre': 'surface', 'pages': 417}
Tax cell establish., Shawn Middleton - measureelizabethstokes@example.com : 2025-01-26 07:56:05.950286+00:00, 4816.63, 253.51, {'genre': 'bar', 'pages': 241}
Whether training campaign., Autumn Hicks - closemorrisdominique@example.net : 2024-03-17 00:23:45.268717+00:00, 2108.65, 9.07, {'genre': 'which', 'pages': 222}
Point soldier., Diane Mata - paperjhill@example.com : 2025-04-04 16:14:51.406967+00:00, 1037.54, 18.98, {'genre': 'future', 'pages': 284}
System beyond special garden., Alicia Dunn - theoryysingleton@example.org : 2024-01-19 09:58:22.640942+00:00, 4373.88, 101.79, {'genre': 'management', 'pages': 298}
Gas wait., Kelly King - peoplelcampbell@example.com : 2024-01-13 22:14:01.107967+00:00, 2589.51, 420.43, {'genre': 'too', 'pages': 119}
Go house., Ralph Thomas - hospitalmendezjames@example.net : 2024-04-24 03:54:07.436451+00:00, 3360.12, 43.53, {'genre': 'case', 'pages': 402}
Power personal evidence., Amber Crawford - dogdaniel39@example.com : 2022-06-19 16:45:21.558637+00:00, 3169.35, 253.44, {'genre': 'population', 'pages': 248}
Discover everyone trip., Joseph Jones - carryhudsonjeremiah@example.com : 2024-10-02 06:02:45.042029+00:00, 1076.52, 176.47, {'genre': 'skill', 'pages': 479}
Movie arrive., George Cantu - calldsmith@example.com : 2023-01-05 20:53:18.709620+00:00, 1038.03, 292.70, {'genre': 'produce', 'pages': 154}
Even find., Dave Brown - challengejakehayes@example.org : 2021-08-20 02:10:00.968014+00:00, 1221.12, 185.70, {'genre': 'personal', 'pages': 500}
List if., Donna Wilson - testohenderson@example.org : 2021-10-28 08:44:40.120808+00:00, 1368.98, 48.08, {'genre': 'tough', 'pages': 381}
Them lead., Andre Ellison - betterpshaffer@example.org : 2022-07-14 02:24:06.621791+00:00, 4278.74, 312.20, {'genre': 'mouth', 'pages': 360}
Commercial floor class., Elizabeth Kline - becauseanthony54@example.com : 2021-10-23 12:51:50.326611+00:00, 1569.69, 229.70, {'genre': 'class', 'pages': 437}
Drive central., Morgan Alvarez - schooltanya26@example.org : 2024-09-02 07:05:13.228538+00:00, 1695.82, 327.06, {'genre': 'wrong', 'pages': 442}
Thousand decide., Joanna Morris - himselfrobertwalker@example.com : 2020-03-14 06:03:24.926150+00:00, 3244.70, 401.80, {'genre': 'themselves', 'pages': 280}
Former wait benefit., Carlos Leonard - thankallenroy@example.com : 2020-03-07 10:01:02.664941+00:00, 2536.40, 401.47, {'genre': 'main', 'pages': 279}
However well to., Douglas Hawkins - southernjennifermiller@example.org : 2020-11-04 13:58:36.747154+00:00, 2744.26, 276.52, {'genre': 'never', 'pages': 302}
Foreign that speech., Melody Norris - manqstewart@example.com : 2021-10-28 11:33:24.821882+00:00, 2088.29, 220.35, {'genre': 'blood', 'pages': 278}
Movie improve course., Jamie Ramirez - catchjohnsonelizabeth@example.org : 2023-01-13 13:52:15.091417+00:00, 3350.22, 279.63, {'genre': 'level', 'pages': 421}
Middle., Jason Parks - secondrobinsonvictor@example.com : 2024-04-02 07:44:04.908302+00:00, 2075.12, 317.24, {'genre': 'onto', 'pages': 361}
Account drive finish., Danielle Wood - enjoythomasgarner@example.com : 2024-11-09 19:29:57.659662+00:00, 3807.63, 76.96, {'genre': 'since', 'pages': 380}
To himself not., Madison Jones - adultemily38@example.org : 2025-02-22 03:54:05.152925+00:00, 1896.61, 151.65, {'genre': 'need', 'pages': 247}
Thus rise., Peter Brewer - rangehernandezdavid@example.net : 2023-05-20 04:24:35.402838+00:00, 3444.06, 104.08, {'genre': 'really', 'pages': 380}
Ok age., Edward Wright - hearreneesanchez@example.net : 2022-03-02 22:30:52.077798+00:00, 1564.42, 198.80, {'genre': 'choose', 'pages': 449}
Analysis mean early., Brandon Lee - describekaren78@example.net : 2020-09-11 08:13:48.979357+00:00, 1098.77, 119.38, {'genre': 'respond', 'pages': 212}
Skill they., Aaron Morales - institutionlaurenallison@example.net : 2024-10-17 20:06:52.000042+00:00, 2183.62, 279.25, {'genre': 'benefit', 'pages': 286}
Century explain rich., Lindsey Conrad - acceptegarcia@example.org : 2023-05-07 09:52:14.338361+00:00, 3657.27, 147.50, {'genre': 'analysis', 'pages': 242}
Bad management large thousand., Andrew Allison - memoryxavier95@example.com : 2024-12-11 01:17:38.324738+00:00, 2379.79, 310.96, {'genre': 'half', 'pages': 197}
Language anything tend., Lori Bennett - performgregory58@example.org : 2021-10-05 15:32:33.777534+00:00, 4270.24, 204.91, {'genre': 'today', 'pages': 144}
Continue teach including., Matthew Morrison - situationfitzgeraldtammy@example.com : 2024-12-12 19:57:52.441907+00:00, 4006.37, 257.40, {'genre': 'after', 'pages': 130}
Apply reality price., Harry Cordova - ownbrianruiz@example.org : 2022-08-18 09:52:29.234945+00:00, 4103.45, 124.89, {'genre': 'politics', 'pages': 389}
College reveal soon., Jennifer Krueger - linejason82@example.com : 2024-09-17 06:08:07.080619+00:00, 4097.20, 137.34, {'genre': 'stock', 'pages': 142}
Road bag., Kenneth Mcneil - knowledgeegrant@example.net : 2022-08-28 02:15:45.323210+00:00, 1948.94, 158.06, {'genre': 'million', 'pages': 203}
Economy include., Mary Mayo - paymwallace@example.net : 2020-12-04 05:13:12.906919+00:00, 4580.46, 166.47, {'genre': 'only', 'pages': 400}

6. Найди все книги с ценой от 750 и выше.
In [25]: for b in list_books:
    ...:     print(b)
    ...: 
Meeting letter mean., Angela Escobar - certainlyhebertrobert@example.com : 2023-02-22 00:37:31.716172+00:00, 3344.98, 312.02, {'genre': 'affect', 'pages': 148}
Professional keep., Victor Kelly - memorymadisonmoore@example.com : 2020-06-28 22:49:55.351064+00:00, 1295.24, 395.76, {'genre': 'player', 'pages': 132}
Meeting environment., Donald Zhang - servemarylewis@example.net : 2023-06-16 10:05:45.086483+00:00, 1168.09, 357.66, {'genre': 'from', 'pages': 131}
New third story., Eric Lee - winclarkdeanna@example.com : 2022-02-07 14:12:54.952720+00:00, 3276.58, 372.19, {'genre': 'data', 'pages': 217}
Exist executive., William Richardson - endtwalker@example.net : 2020-03-22 04:05:09.242319+00:00, 4121.63, 251.97, {'genre': 'soldier', 'pages': 262}
Fear., Brandon Mcknight - eventheresa60@example.org : 2023-11-25 02:28:17.794569+00:00, 2339.26, 88.25, {'genre': 'writer', 'pages': 490}
Break nation., Bonnie Hess - alonekimberlywilliams@example.com : 2024-07-30 21:59:22.048699+00:00, 855.60, 344.45, {'genre': 'theory', 'pages': 212}
Beyond respond consider., Harold Wagner - nearlyahenry@example.org : 2024-02-24 20:06:18.649125+00:00, 4567.98, 334.74, {'genre': 'unit', 'pages': 468}
According might tend., Amber Glover - roleycordova@example.net : 2022-12-10 22:52:37.428110+00:00, 778.90, 220.35, {'genre': 'great', 'pages': 156}
Explain store general., Corey Blackwell - agobecky22@example.org : 2021-05-18 14:19:34.280770+00:00, 4397.39, 184.80, {'genre': 'under', 'pages': 195}
Painting decide., Erin Robinson - awayafisher@example.com : 2021-01-13 05:48:47.603779+00:00, 2834.37, 227.06, {'genre': 'though', 'pages': 148}
To seem live., Kelly Wong - professorduncanzachary@example.net : 2025-06-15 18:10:38.601416+00:00, 3554.58, 289.80, {'genre': 'opportunity', 'pages': 451}
Fact very., Billy Valentine - arrivelongvanessa@example.com : 2020-09-01 20:10:07.733161+00:00, 1900.60, 56.77, {'genre': 'middle', 'pages': 460}
Low., Eric Green - dealggarcia@example.org : 2020-09-08 19:34:08.540429+00:00, 2600.32, 437.09, {'genre': 'best', 'pages': 344}
Sing., Stephanie Castro - wondermelissa45@example.net : 2021-01-27 23:32:18.693934+00:00, 3792.01, 20.85, {'genre': 'defense', 'pages': 137}
Personal., Kelly Hardy - leastgarciaryan@example.net : 2020-06-14 21:58:05.944401+00:00, 4295.98, 161.00, {'genre': 'store', 'pages': 340}
Instead thank., Nicole Jimenez - firstchristopher00@example.com : 2023-08-26 03:21:51.787934+00:00, 3845.65, 341.32, {'genre': 'popular', 'pages': 174}
Industry large., John Romero - voicerogersmark@example.org : 2020-03-02 08:03:39.600936+00:00, 1526.15, 67.95, {'genre': 'agreement', 'pages': 232}
Adult once lead., Eric Stevenson - commercialcheryl05@example.net : 2022-01-29 12:48:04.840868+00:00, 4797.42, 135.98, {'genre': 'sport', 'pages': 108}
Political fire., Carlos Bird - preparesgarrison@example.net : 2020-10-23 10:09:45.968190+00:00, 3244.97, 289.99, {'genre': 'exactly', 'pages': 493}
Travel college condition., Brittany Harding - explainlisa82@example.org : 2022-11-28 08:49:14.605953+00:00, 3732.66, 359.33, {'genre': 'range', 'pages': 446}
Step accept senior., Angela Ayers - thoughtakramer@example.org : 2021-09-22 08:32:39.470432+00:00, 3287.96, 175.65, {'genre': 'prove', 'pages': 406}
We current popular., Michele Williamson - strongjosephjones@example.org : 2024-08-25 13:31:12.192678+00:00, 3798.76, 407.86, {'genre': 'second', 'pages': 267}
Shake take law., Brittany Mcfarland - internationaluporter@example.net : 2021-12-24 07:11:00.353744+00:00, 4098.23, 60.53, {'genre': 'police', 'pages': 218}
Ask TV., Christopher Rogers - billamberjones@example.com : 2024-10-10 20:23:04.896218+00:00, 2844.66, 320.46, {'genre': 'near', 'pages': 451}
Sort morning., Savannah King - ableowood@example.com : 2020-01-02 01:29:47.573082+00:00, 4190.75, 67.15, {'genre': 'that', 'pages': 142}
Your value., Margaret Pena - purposebridgetdavis@example.org : 2025-04-06 06:03:55.901639+00:00, 4257.08, 2.16, {'genre': 'reality', 'pages': 204}
Television business., Gary Martin - futurerichardsonerica@example.net : 2020-02-12 17:17:38.004358+00:00, 3446.25, 436.92, {'genre': 'contain', 'pages': 155}
One office against., Luke Duarte - windobrown@example.net : 2020-01-27 00:04:59.042336+00:00, 3002.12, 441.30, {'genre': 'where', 'pages': 332}
Example behind., Kristina Taylor - heavyufleming@example.com : 2021-07-01 19:39:06.748351+00:00, 4478.69, 366.30, {'genre': 'firm', 'pages': 150}
Move hand., Karen Reyes - centralmcleanfrank@example.org : 2022-10-26 10:12:40.893220+00:00, 3578.45, 11.17, {'genre': 'even', 'pages': 299}
Professional fall peace., John Kane - bodyjohnsonalexandria@example.net : 2022-10-22 04:45:37.603637+00:00, 2812.32, 136.52, {'genre': 'window', 'pages': 400}
Much myself born sometimes., Jeffrey Taylor - PMamarquez@example.org : 2023-10-05 14:36:01.704642+00:00, 903.83, 1.06, {'genre': 'short', 'pages': 121}
Fire suffer around radio., Chad Dunn - investmenturamos@example.net : 2024-09-15 19:47:58.925880+00:00, 2818.96, 375.67, {'genre': 'mother', 'pages': 259}
Season start., Robert Graves - sixmichelle76@example.com : 2024-09-13 06:46:21.382140+00:00, 1403.68, 430.87, {'genre': 'kitchen', 'pages': 164}
Total usually., Jorge Mcdowell - westernmendozaandrew@example.org : 2022-05-05 01:59:54.107788+00:00, 1397.07, 422.65, {'genre': 'site', 'pages': 180}
Shake no., Rachel Goodwin - fourbflores@example.net : 2022-09-01 08:04:53.139424+00:00, 882.26, 308.92, {'genre': 'hold', 'pages': 345}
Cut hotel., Jonathan Elliott - Mrdanielwright@example.org : 2021-06-11 04:59:18.930929+00:00, 1464.49, 243.78, {'genre': 'yourself', 'pages': 366}
Perform., Andrea Arnold - cityrhill@example.org : 2023-02-04 02:14:07.528152+00:00, 1222.16, 133.04, {'genre': 'reality', 'pages': 395}
Next top., Brianna Long - motherbrandonperry@example.org : 2022-10-03 06:39:37.601050+00:00, 2992.80, 286.05, {'genre': 'impact', 'pages': 170}
Pressure., Colleen Roberts - sourcecarlsonchristopher@example.com : 2021-11-05 14:47:56.033042+00:00, 1555.03, 42.70, {'genre': 'either', 'pages': 498}
Dog something., Brittany Harding - explainlisa82@example.org : 2025-01-07 01:15:50.357448+00:00, 3630.33, 259.81, {'genre': 'little', 'pages': 285}
Season interest., Lauren Jenkins - phonejohnstonjoyce@example.com : 2022-01-17 06:51:45.909125+00:00, 3088.07, 149.07, {'genre': 'finish', 'pages': 330}
Here choose worker., Sheila Todd - sorttedwards@example.com : 2020-12-20 21:12:45.102972+00:00, 2517.95, 216.62, {'genre': 'player', 'pages': 306}
Kitchen material lose., Denise Hall - thosejohnreyes@example.org : 2024-08-20 15:11:40.577817+00:00, 4226.24, 431.06, {'genre': 'reality', 'pages': 311}
Source probably check., Paul Webster - whilepalmersierra@example.com : 2022-01-26 20:40:47.079689+00:00, 4384.55, 225.88, {'genre': 'plan', 'pages': 224}
Sell where., Edward Williams - structuresmithhannah@example.org : 2023-01-05 23:43:20.531107+00:00, 2834.86, 422.92, {'genre': 'culture', 'pages': 148}
Forget picture yard., Robert Holmes - specialharrisjamie@example.com : 2023-01-12 10:16:55.217300+00:00, 3675.25, 258.50, {'genre': 'interesting', 'pages': 281}
Author try charge., John Smith - statementjackhardy@example.org : 2024-01-17 17:29:27.206612+00:00, 4769.70, 370.92, {'genre': 'it', 'pages': 293}
Account cover pick., Sarah Hall - againstdonaldali@example.org : 2025-04-19 15:50:15.471072+00:00, 3791.59, 107.01, {'genre': 'follow', 'pages': 345}

### Поиск текста
7. Найди все книги, содержащие слово «django» в названии.  
In [26]: list_books = Book.objects.filter(title__icontains='django')
In [27]: list_books
Out[27]: <QuerySet []>

8. Найди книги, в названии которых есть «python» (без учёта регистра).  
In [30]: list_books = Book.objects.filter(title__icontains='python')
In [31]: list_books
Out[31]: <QuerySet []>

9. Найди книги, название которых начинается со слова «Advanced».
In [33]: list_books = Book.objects.filter(title__startswith='Advanced')
In [35]: list_books
Out[35]: <QuerySet []> 

10. Найди книги, название которых начинается с «pro» (игнорируя регистр).  
In [38]: list_books = Book.objects.filter(title__istartswith='pro')
In [40]: for b in list_books:
    ...:     print(b)
    ...: 
Professional keep., Victor Kelly - memorymadisonmoore@example.com : 2020-06-28 22:49:55.351064+00:00, 1295.24, 395.76, {'genre': 'player', 'pages': 132}
Professional fall peace., John Kane - bodyjohnsonalexandria@example.net : 2022-10-22 04:45:37.603637+00:00, 2812.32, 136.52, {'genre': 'window', 'pages': 400}
Protect drug., Angela Shaw - weekohumphrey@example.com : 2023-04-10 05:58:22.841906+00:00, 596.32, 282.24, {'genre': 'benefit', 'pages': 175}
Protect how., Katherine Lowe - gocarlsonmelinda@example.net : 2021-11-21 10:59:30.226649+00:00, 3226.22, 419.83, {'genre': 'woman', 'pages': 473}
Process few resource., Kenneth Hart - whomjoseph81@example.com : 2022-06-23 10:34:50.001297+00:00, 2234.05, 330.23, {'genre': 'idea', 'pages': 137}
Prove wear friend., Sarah Montes - truthheather87@example.net : 2023-07-15 06:00:26.428263+00:00, 2502.46, 68.94, {'genre': 'his', 'pages': 240}
Product pick parent., Carolyn Durham - seasonchristopherroman@example.com : 2024-08-18 14:14:21.354476+00:00, 4081.64, 235.89, {'genre': 'environmental', 'pages': 110}
Project responsibility., Brandon Lee - describekaren78@example.net : 2024-07-20 07:39:50.663056+00:00, 4259.27, 359.71, {'genre': 'expect', 'pages': 484}
Project after next., Daniel Sullivan - anyppayne@example.net : 2024-10-22 09:18:24.135454+00:00, 3456.71, 414.31, {'genre': 'different', 'pages': 407}
Program recently., James Hicks - voicegreerselena@example.net : 2021-05-19 00:38:19.400773+00:00, 3054.96, 56.52, {'genre': 'hear', 'pages': 454}
Professor brother., Larry Crawford - publichallbrandon@example.net : 2023-06-23 17:42:28.165646+00:00, 3423.73, 101.02, {'genre': 'anything', 'pages': 340}
Project go be., Joseph Jackson - hourtashapierce@example.net : 2024-04-03 02:09:00.916012+00:00, 656.78, 7.92, {'genre': 'too', 'pages': 189}
Protect left either., Joanne Gibson - richjudywillis@example.org : 2020-05-06 06:46:21.844753+00:00, 3142.47, 56.46, {'genre': 'table', 'pages': 294}
Protect yet community understand., Angela Brown - eachdenise34@example.net : 2023-08-11 03:53:56.817436+00:00, 3860.82, 228.56, {'genre': 'live', 'pages': 389}
Prove of city., Joel James - southvayers@example.org : 2021-12-11 05:33:00.282902+00:00, 1527.55, 421.80, {'genre': 'fast', 'pages': 239}
Project eye on., Jonathan Hernandez - culturecreyes@example.org : 2022-12-25 23:43:55.569351+00:00, 2127.40, 111.03, {'genre': 'kid', 'pages': 114}
Production spend cover., Alexander Sanchez - militarysaraboone@example.com : 2025-03-04 10:01:25.191429+00:00, 4161.84, 425.32, {'genre': 'concern', 'pages': 450}
Process left., Raven Smith - costashley43@example.com : 2022-02-03 05:34:12.026409+00:00, 4207.48, 177.11, {'genre': 'find', 'pages': 426}
Property Congress child., Susan Bauer - magazinetmason@example.org : 2020-09-05 03:32:35.658586+00:00, 3806.92, 444.81, {'genre': 'miss', 'pages': 390}
Production teacher with level., Robert Brooks - playermfernandez@example.org : 2024-02-20 03:07:11.156751+00:00, 907.61, 442.12, {'genre': 'house', 'pages': 168}
Protect adult., Leah Marsh - listenrandy46@example.org : 2020-08-12 09:23:51.571423+00:00, 2141.78, 96.41, {'genre': 'sea', 'pages': 323}
Program religious., Lisa Jefferson - goortegagary@example.net : 2023-06-09 12:24:23.944496+00:00, 2487.50, 113.20, {'genre': 'realize', 'pages': 237}
Provide play., Crystal Banks - sistergoldenleslie@example.com : 2020-10-20 15:45:23.323810+00:00, 4716.86, 307.70, {'genre': 'rule', 'pages': 431}
Project bag., Samuel Martin - whitejennifer35@example.com : 2025-03-14 12:01:40.956889+00:00, 2264.12, 12.24, {'genre': 'remain', 'pages': 298}
Prove itself whose about., Rebecca Snyder - historyanthonyhughes@example.com : 2022-01-24 21:02:28.026787+00:00, 3918.85, 77.50, {'genre': 'defense', 'pages': 454}
Property view., Katelyn Perez - agentkayla43@example.org : 2022-12-02 12:48:46.219351+00:00, 1088.40, 414.06, {'genre': 'heavy', 'pages': 326}
Professor appear phone., Joseph Griffin - muchbrownangela@example.net : 2021-07-14 20:42:29.888822+00:00, 2337.26, 377.32, {'genre': 'central', 'pages': 274}
Program see., Adam Delacruz - summerjohnmarks@example.org : 2023-04-14 15:18:09.483932+00:00, 2529.97, 160.62, {'genre': 'material', 'pages': 397}
Professional not career., Kathryn Short - paymakaylathomas@example.com : 2021-01-02 04:03:56.756568+00:00, 4123.52, 419.61, {'genre': 'usually', 'pages': 104}
Professor., Juan Anderson - childrobertbates@example.net : 2025-04-17 03:53:45.555941+00:00, 539.02, 372.05, {'genre': 'break', 'pages': 293}
Process., Kelly Johnson - schoolgavin30@example.com : 2022-09-25 14:45:00.618238+00:00, 1903.45, 4.52, {'genre': 'ago', 'pages': 403}
Project reveal democratic daughter., Linda Owens - eitherangela42@example.com : 2024-05-05 16:23:17.997304+00:00, 1713.82, 263.60, {'genre': 'Democrat', 'pages': 408}
Property operation., Charlotte Pruitt - foreignjohnsonclifford@example.org : 2022-06-07 09:48:33.408303+00:00, 591.76, 220.74, {'genre': 'simple', 'pages': 132}
Professor out direction., Nathan Walker - frontjames88@example.org : 2020-07-21 06:00:30.893354+00:00, 3971.92, 228.75, {'genre': 'add', 'pages': 311}
Product lose admit., Erik Flores - towardscotttracy@example.com : 2023-10-23 09:51:21.874484+00:00, 1655.52, 103.86, {'genre': 'together', 'pages': 495}
Production sound., Aaron Morales - institutionlaurenallison@example.net : 2022-05-20 15:14:58.991078+00:00, 1842.24, 106.72, {'genre': 'she', 'pages': 439}
Program keep., Marco Owens - guessrobinking@example.net : 2024-01-22 11:16:27.056660+00:00, 2593.56, 114.51, {'genre': 'town', 'pages': 274}
Produce response., Raymond Johnson - watchnhale@example.com : 2020-04-07 05:20:21.128458+00:00, 558.53, 124.29, {'genre': 'whatever', 'pages': 168}
Produce evidence., Allison Fowler - recordzerickson@example.net : 2022-04-15 04:25:23.863303+00:00, 2143.00, 221.93, {'genre': 'guy', 'pages': 273}
Property remain year., Lisa Russell - tengutierrezkristina@example.net : 2025-04-24 11:16:12.812379+00:00, 2725.33, 33.34, {'genre': 'situation', 'pages': 123}
Product begin., Lindsey Lynch - outdwells@example.org : 2021-11-04 07:25:38.265864+00:00, 4775.58, 89.21, {'genre': 'research', 'pages': 375}
Prove hear., Jonathon Sanders - latejoseph27@example.org : 2022-01-06 18:16:01.628659+00:00, 3673.58, 121.82, {'genre': 'democratic', 'pages': 269}
Professor strong nothing international., Margaret Pena - purposebridgetdavis@example.org : 2022-03-27 21:46:43.389121+00:00, 4588.96, 131.92, {'genre': 'serve', 'pages': 390}
Program nature bring treatment., John Kemp - considergoodmanandre@example.org : 2020-06-16 10:54:50.958668+00:00, 4413.75, 160.24, {'genre': 'understand', 'pages': 448}
Production particularly., Bryan Nelson - enternwalker@example.org : 2025-06-08 05:05:11.413539+00:00, 4471.01, 326.63, {'genre': 'democratic', 'pages': 345}
Prove property prove., Jamie Ramirez - catchjohnsonelizabeth@example.org : 2023-12-04 16:42:58.380198+00:00, 4045.04, 61.81, {'genre': 'common', 'pages': 311}
Prove too try., Matthew Wood - discoverqmitchell@example.com : 2022-06-06 08:40:45.118605+00:00, 3966.02, 159.17, {'genre': 'east', 'pages': 332}
Process commercial for., Jasmine Blankenship - bigtoni79@example.net : 2025-02-09 08:44:34.564495+00:00, 4374.20, 380.89, {'genre': 'beat', 'pages': 145}
Prove man yet., Sharon Davidson - orlbrooks@example.org : 2023-01-25 10:43:01.073094+00:00, 555.63, 370.30, {'genre': 'tend', 'pages': 135}
Protect best successful., Raven Smith - costashley43@example.com : 2023-03-30 12:37:25.287620+00:00, 4707.61, 134.75, {'genre': 'score', 'pages': 485}
Produce eye amount., Amber Wood - treeisandoval@example.com : 2024-12-14 01:40:11.512713+00:00, 4219.99, 384.73, {'genre': 'current', 'pages': 433}
Prove century., Jennifer Thompson - preparewilliamsmith@example.org : 2022-10-30 07:24:45.438225+00:00, 4655.88, 218.16, {'genre': 'subject', 'pages': 353}
Provide work., Carlos Sanders - letclarkamanda@example.net : 2021-04-05 12:09:48.167789+00:00, 2006.13, 3.83, {'genre': 'form', 'pages': 201}
Process myself., James Cardenas - factoroy@example.net : 2024-12-07 20:54:31.189100+00:00, 4034.97, 48.32, {'genre': 'house', 'pages': 121}
Produce half window., Deborah Williams - owntravis68@example.net : 2023-08-02 02:11:50.924291+00:00, 4143.94, 425.40, {'genre': 'door', 'pages': 344}
Prove understand., Victoria Morgan - sevenlisaparker@example.com : 2024-05-20 04:31:08.529257+00:00, 2342.55, 98.29, {'genre': 'girl', 'pages': 469}
Protect wear., Christopher Parker - religiouserikaholloway@example.net : 2025-06-28 16:02:21.934930+00:00, 2958.95, 390.35, {'genre': 'deal', 'pages': 208}
Professional yet., Richard Brown - latercaitlinsalazar@example.com : 2022-12-09 14:32:52.625813+00:00, 1353.44, 174.30, {'genre': 'position', 'pages': 114}
Provide might recognize., Robert Brooks - personcindy64@example.com : 2021-04-24 00:27:34.215661+00:00, 2346.01, 393.94, {'genre': 'choice', 'pages': 102}
Process think identify., Becky Jones - thiselizabeth81@example.com : 2023-05-24 08:24:56.917540+00:00, 1744.56, 34.72, {'genre': 'technology', 'pages': 393}
Product never., Joshua Watson - containwallacebrandy@example.org : 2023-02-28 03:25:57.228662+00:00, 3805.43, 141.89, {'genre': 'during', 'pages': 111}
Professor point probably claim., Eric Sheppard - forgetaaron28@example.net : 2023-03-21 16:03:46.119415+00:00, 4533.35, 383.91, {'genre': 'year', 'pages': 202}
Program relationship increase., Steven Banks - headvelasquezjennifer@example.com : 2024-04-23 12:33:11.595220+00:00, 1253.09, 139.67, {'genre': 'practice', 'pages': 485}
Project actually everything law., Tammy Melton - waterpatrick25@example.org : 2022-11-14 14:55:51.404048+00:00, 3326.57, 168.73, {'genre': 'magazine', 'pages': 468}
Program security control., Brooke Contreras - charactercourtneydurham@example.org : 2024-07-15 04:54:15.917455+00:00, 2692.62, 42.55, {'genre': 'quality', 'pages': 140}
Process., Brittney Rodgers - agojonathan32@example.com : 2024-06-17 20:04:08.612889+00:00, 1475.18, 11.74, {'genre': 'truth', 'pages': 312}
Production human those., Robert Gonzalez - fourjasminemiller@example.com : 2025-06-12 01:23:40.031980+00:00, 4245.02, 149.87, {'genre': 'land', 'pages': 294}
Product cultural., Anthony Shaw - actuallybellis@example.com : 2024-08-30 07:00:34.937452+00:00, 1020.87, 446.65, {'genre': 'present', 'pages': 173}
Probably long everyone., Erik Flores - towardscotttracy@example.com : 2021-11-08 00:50:18.626296+00:00, 4046.77, 382.78, {'genre': 'nothing', 'pages': 239}
Process protect tonight., David Bryant - dobrittanyclark@example.com : 2020-01-25 03:35:40.566963+00:00, 1527.96, 374.04, {'genre': 'concern', 'pages': 239}
Produce worry look., Jeremy Stewart - everytoddnancy@example.net : 2025-03-26 14:25:07.288827+00:00, 2828.42, 31.13, {'genre': 'space', 'pages': 338}
Process able meeting., Gene Collins - butdnguyen@example.com : 2021-10-24 08:08:13.930269+00:00, 3445.70, 278.73, {'genre': 'study', 'pages': 202}
Produce project social., Jonathan Hartman - arguekelly77@example.com : 2020-09-01 15:02:05.579993+00:00, 4021.34, 314.59, {'genre': 'cultural', 'pages': 167}
Process plan general., Larry Boyle - tonightjasonsmith@example.org : 2023-04-13 10:54:46.877554+00:00, 1582.89, 254.87, {'genre': 'heart', 'pages': 433}
Program future pick., Jason Parks - secondrobinsonvictor@example.com : 2021-03-23 13:34:08.772949+00:00, 3219.94, 91.63, {'genre': 'word', 'pages': 283}
Provide visit., Sandra Harrington - machinepetersendavid@example.org : 2023-12-15 00:59:57.281204+00:00, 3725.06, 59.69, {'genre': 'statement', 'pages': 104}
Production amount follow film., Jeffery Rose - anothermarywright@example.com : 2021-09-23 00:37:51.375990+00:00, 934.39, 65.58, {'genre': 'sure', 'pages': 285}
Probably agent., Jessica Walls - establishswilliams@example.com : 2022-07-25 06:20:21.356130+00:00, 2324.55, 245.76, {'genre': 'song', 'pages': 351}
Property none conference., Heather Green - assumemeghan64@example.org : 2023-05-23 10:41:49.810231+00:00, 2902.18, 92.03, {'genre': 'sense', 'pages': 162}
Project result beat., William Schroeder - youcjames@example.net : 2021-01-10 06:17:50.208159+00:00, 3409.27, 370.72, {'genre': 'put', 'pages': 161}
Professional nature across., Jessica Miller - wifechristinaparker@example.net : 2024-10-13 10:20:55.442494+00:00, 2284.99, 329.58, {'genre': 'kitchen', 'pages': 356}
Production capital., Courtney Reed - southernflowersjohn@example.com : 2024-12-19 18:34:15.593801+00:00, 2634.55, 388.51, {'genre': 'speak', 'pages': 254}
Program not although., Bonnie Bowman - reallyhwatson@example.net : 2022-03-23 18:16:32.078273+00:00, 3462.71, 109.91, {'genre': 'likely', 'pages': 321}
Produce next., Heidi Wheeler - conferencebalexander@example.net : 2024-07-27 19:01:37.226702+00:00, 3184.15, 275.78, {'genre': 'admit', 'pages': 431}
Probably look growth., Brooke Contreras - charactercourtneydurham@example.org : 2021-12-20 04:25:55.566012+00:00, 2832.86, 386.52, {'genre': 'tend', 'pages': 496}
Production each., Donald Middleton - authorityantonio91@example.com : 2020-07-14 03:31:17.945915+00:00, 2732.99, 149.95, {'genre': 'thus', 'pages': 248}
Probably property., Susan Hernandez - picktoddgraves@example.org : 2020-05-20 09:25:59.441551+00:00, 964.86, 301.31, {'genre': 'teach', 'pages': 319}
Program man cut., Marcus Farmer - particularbriggssean@example.net : 2020-08-12 22:38:26.938531+00:00, 3010.70, 8.81, {'genre': 'myself', 'pages': 123}
Program recognize want., Elizabeth Smith - useplee@example.net : 2021-04-01 03:29:44.437364+00:00, 695.11, 380.84, {'genre': 'station', 'pages': 257}
Project you loss., Ruben Hill - continuestevenholmes@example.net : 2023-07-31 13:07:15.350766+00:00, 966.62, 11.42, {'genre': 'force', 'pages': 235}
Program., Elizabeth Branch - oilkstephens@example.org : 2023-10-13 07:38:03.326614+00:00, 4480.25, 134.85, {'genre': 'act', 'pages': 109}
Probably Republican difference time., Cathy Edwards - propertycopelandkelsey@example.com : 2021-03-30 18:29:38.638282+00:00, 2572.23, 192.47, {'genre': 'eye', 'pages': 169}
Production cultural agree., Jennifer Robinson - officejason21@example.com : 2020-11-20 16:23:50.736401+00:00, 1696.35, 286.73, {'genre': 'degree', 'pages': 102}
Product artist middle box., Melissa Stone - edgewchristian@example.org : 2022-10-17 21:04:48.097008+00:00, 4312.51, 139.59, {'genre': 'dream', 'pages': 180}
Production story than blue., Lisa Baldwin - trainingandersontyler@example.com : 2022-07-26 16:45:49.687537+00:00, 2027.79, 208.80, {'genre': 'clearly', 'pages': 373}
Process news himself., Johnny Bradley - politicsangela12@example.net : 2020-02-16 12:34:07.633815+00:00, 3199.73, 412.43, {'genre': 'technology', 'pages': 440}
Product exactly along., Richard Burke - insidelauren15@example.com : 2025-05-23 12:35:24.311196+00:00, 1064.51, 68.87, {'genre': 'green', 'pages': 378}
Provide source., Taylor Black - somehannah98@example.org : 2024-08-15 04:05:47.806974+00:00, 1175.74, 287.59, {'genre': 'above', 'pages': 373}
Program since social., Lisa Russell - tengutierrezkristina@example.net : 2020-07-11 00:06:42.479609+00:00, 1056.40, 149.08, {'genre': 'piece', 'pages': 294}
Property remember., Jonathan Silva - musicstonejeffery@example.org : 2025-05-16 08:07:31.396525+00:00, 3497.74, 164.59, {'genre': 'assume', 'pages': 362}
Program imagine lead., Timothy Patel - updfrederick@example.org : 2021-06-26 08:15:12.565408+00:00, 1648.15, 206.42, {'genre': 'stage', 'pages': 306}
Probably she build., William Kline - verycaitlin04@example.com : 2020-07-25 10:16:43.696805+00:00, 733.47, 48.72, {'genre': 'be', 'pages': 498}
Produce from success walk., Maurice Smith - nicewatkinsnathan@example.org : 2025-05-23 21:09:15.336220+00:00, 1752.35, 103.61, {'genre': 'forget', 'pages': 201}
Project debate., Megan Carter - governmentmichael26@example.com : 2020-03-31 06:37:55.652080+00:00, 2684.60, 72.89, {'genre': 'continue', 'pages': 220}
Property campaign management., Christine Cooper - treatnelsonfrederick@example.net : 2024-10-02 06:17:58.998113+00:00, 1582.99, 98.51, {'genre': 'weight', 'pages': 265}
Property voice call., Amber Diaz - thesegonzalezeric@example.net : 2021-12-15 20:58:59.414552+00:00, 4450.12, 425.61, {'genre': 'center', 'pages': 281}
Product model fire expect., William Kline - verycaitlin04@example.com : 2020-11-23 11:00:08.527199+00:00, 1969.43, 315.56, {'genre': 'soldier', 'pages': 102}
Product per space., Donna Odonnell - flylaura15@example.com : 2023-03-23 17:43:44.036598+00:00, 1639.35, 206.95, {'genre': 'board', 'pages': 335}
Project kind., Bryan Davis - easygarzasteven@example.net : 2022-10-24 05:29:20.699561+00:00, 679.00, 27.63, {'genre': 'fish', 'pages': 304}
Production able add., Joseph Perez - seatbeckybarnett@example.com : 2023-05-11 01:19:22.710318+00:00, 2649.75, 78.44, {'genre': 'prepare', 'pages': 331}
Produce plant wife., Matthew Morrison - situationfitzgeraldtammy@example.com : 2021-01-21 15:32:03.097108+00:00, 1861.10, 25.95, {'genre': 'itself', 'pages': 466}
Produce talk., Michael Henderson - alsodebraavila@example.com : 2021-07-04 04:33:40.182932+00:00, 1789.33, 291.63, {'genre': 'real', 'pages': 409}
Production drug everybody., Edward Williams - structuresmithhannah@example.org : 2020-07-12 02:53:39.612466+00:00, 4376.27, 188.96, {'genre': 'security', 'pages': 169}
Provide interview inside., James Pace - understandcolemanamy@example.org : 2020-02-26 08:36:42.113650+00:00, 1429.48, 397.34, {'genre': 'evidence', 'pages': 466}
Probably language learn., James Rose - daughterdustin94@example.net : 2022-05-20 01:39:44.071592+00:00, 4739.65, 105.10, {'genre': 'decide', 'pages': 176}
Probably live until., Ryan Olson - jointheresatucker@example.net : 2020-05-17 21:32:39.118961+00:00, 2884.02, 359.10, {'genre': 'include', 'pages': 461}
Professional themselves., Samuel Martin - whitejennifer35@example.com : 2022-11-05 06:13:37.931741+00:00, 4938.08, 178.57, {'genre': 'against', 'pages': 208}
Produce either ability plan., Terri Kennedy - stayfmoore@example.com : 2023-05-25 00:42:03.685776+00:00, 1779.75, 346.68, {'genre': 'senior', 'pages': 104}
Provide fill., Randy Smith - startvanessahoward@example.net : 2021-04-01 08:11:15.285960+00:00, 3876.21, 440.60, {'genre': 'whole', 'pages': 414}
Project quite., Anthony Meyers - formmmaynard@example.net : 2023-03-28 13:24:01.041432+00:00, 4732.57, 258.14, {'genre': 'though', 'pages': 257}
Produce upon., Michael Miller - effectchristinajenkins@example.net : 2021-05-09 00:32:00.983179+00:00, 1364.01, 430.99, {'genre': 'less', 'pages': 186}
Property laugh trade., Anthony Duffy - foothkeller@example.com : 2022-12-10 10:20:05.743207+00:00, 2788.28, 216.92, {'genre': 'entire', 'pages': 353}
Produce difference little., Sarah Patel - ownbrownsheila@example.com : 2023-09-06 11:23:33.279709+00:00, 1965.92, 0.58, {'genre': 'provide', 'pages': 429}
Process., Deborah Gregory - informationihansen@example.com : 2020-11-01 22:21:56.324911+00:00, 1095.66, 186.47, {'genre': 'appear', 'pages': 213}
Prove beautiful., Angela Ayers - thoughtakramer@example.org : 2020-08-02 17:30:12.184083+00:00, 3878.47, 203.38, {'genre': 'wife', 'pages': 343}
Prove morning., Samuel Gomez - rateocarr@example.net : 2024-10-26 23:28:09.033679+00:00, 1839.71, 444.44, {'genre': 'food', 'pages': 243}
Protect meeting., Nicholas Rodriguez - leastlisalopez@example.com : 2020-01-11 05:38:16.755664+00:00, 3712.34, 349.38, {'genre': 'manager', 'pages': 480}
Provide financial same., Hector Barnes - conditiondaniel21@example.org : 2021-11-12 01:39:10.718628+00:00, 4823.38, 90.15, {'genre': 'old', 'pages': 188}
Process Mrs some., Vanessa Brown - threethomasdavid@example.com : 2024-08-18 16:34:35.863273+00:00, 4325.85, 333.81, {'genre': 'color', 'pages': 461}

11. Найди книги, название которых заканчивается на слово «Guide».  
In [44]: list_books = Book.objects.filter(title__endswith='Guide')
In [45]: list_books
Out[45]: <QuerySet []>

12. Найди книги, название которых заканчивается на «tutorial» (без учёта регистра).
In [46]: list_books = Book.objects.filter(title__iendswith='tutorial')
In [47]: list_books
Out[47]: <QuerySet []>

### Проверка на null
13. Найди все отзывы без комментариев.  
In [55]: list_reviews = Review.objects.filter(comment__isnull=True)
In [56]: list_reviews
Out[56]: <QuerySet []>
In [57]: list_reviews = Review.objects.filter(comment='')
In [58]: list_reviews
Out[58]: <QuerySet []>
In [59]: list_reviews = Review.objects.exclude(comment='').exclude(comment__isnull=True)[:50]
In [60]: for r in list_reviews:
    ...:     print(r)
    ...: 
Eight without., Donald Phillips - althoughdavistammy@example.com : 2022-12-06 18:36:14.579380+00:00, 2606.54, 446.68, {'genre': 'both', 'pages': 265}: 1, Nothing blood way modern by make medical positive never at work pull food.
Star owner., David Hicks - withoutalexander75@example.net : 2021-07-26 11:02:01.339512+00:00, 3322.33, 435.53, {'genre': 'create', 'pages': 463}: 1, President sign administration speak especially out tough girl since until contain.
Work also professional., Laura Sims - everythingrperry@example.net : 2022-03-29 07:59:25.824909+00:00, 4901.08, 321.75, {'genre': 'strategy', 'pages': 178}: 1, Interview ahead point wish cup attorney heart budget lot.
Visit start lead., Catherine Houston - goalamartinez@example.net : 2020-07-21 03:34:32.830353+00:00, 3452.20, 191.84, {'genre': 'wonder', 'pages': 483}: 1, Old factor purpose report century pass institution after wonder may course.
Year agree., Anna Flores - identifyjhill@example.org : 2025-07-04 18:12:58.279652+00:00, 1064.63, 47.82, {'genre': 'notice', 'pages': 336}: 4, Cost yard add figure investment ten surface impact citizen however.
Involve tell for., Elizabeth Harrington - allowdylanstevens@example.net : 2023-10-09 07:29:35.190818+00:00, 3924.65, 102.68, {'genre': 'relationship', 'pages': 394}: 4, Notice pattern administration practice national sister remember government institution answer president.
Along next history., Jonathan Hayes - riskmelissamontgomery@example.org : 2024-11-11 13:38:08.170292+00:00, 3933.46, 93.81, {'genre': 'size', 'pages': 264}: 4, Stay great smile raise body front challenge relate base sure grow.
During friend floor., Taylor Jones - asharrissusan@example.net : 2022-06-12 12:52:08.491629+00:00, 1095.77, 420.31, {'genre': 'need', 'pages': 465}: 5, Chance along child large dinner air girl.
Number into., William Kline - verycaitlin04@example.com : 2025-01-07 05:16:17.166077+00:00, 2239.79, 292.38, {'genre': 'standard', 'pages': 255}: 3, Charge and situation ok step success suddenly sport song despite soldier seem agency age.
North it., Melissa Smith - paintingcampbelltony@example.org : 2025-06-04 23:12:46.578654+00:00, 3031.29, 176.94, {'genre': 'teach', 'pages': 343}: 1, Cultural pay stage time beautiful young through today full receive class view action.
Last believe help., Jacob Decker - withoutcgrant@example.org : 2023-10-31 06:22:18.541118+00:00, 2638.01, 391.43, {'genre': 'whole', 'pages': 323}: 5, Top down account finish memory front sometimes technology.
Beyond either reach., Anthony Wright - starucamacho@example.com : 2023-09-10 14:22:00.208025+00:00, 1492.87, 275.52, {'genre': 'up', 'pages': 272}: 3, Above spend get defense skin travel keep finish yard young.
At office., Jaclyn Smith - behindzimmermanemily@example.org : 2021-09-09 16:28:09.193849+00:00, 2722.26, 28.48, {'genre': 'officer', 'pages': 114}: 2, Bit style real rather break particular along.
Bag rich marriage., Angela Fox - uscmack@example.org : 2024-04-18 15:19:23.967329+00:00, 2279.49, 410.53, {'genre': 'must', 'pages': 337}: 5, Part education prevent worker name find support only what agent.
Certain main dark., Monica Hardin - nightpyoung@example.net : 2023-07-27 18:41:34.952261+00:00, 1365.63, 20.24, {'genre': 'agreement', 'pages': 123}: 1, Reflect ability street hour process begin question yes let food commercial perhaps piece.
Fish want main., Craig Gillespie - citizenlluna@example.com : 2020-12-12 20:41:34.377458+00:00, 2678.34, 370.93, {'genre': 'federal', 'pages': 119}: 5, Moment chair executive design such important raise difficult.
Individual important laugh., Brandi Robinson - believejohn85@example.org : 2024-04-08 02:56:53.866121+00:00, 1614.32, 315.45, {'genre': 'often', 'pages': 152}: 1, Require leave manager yeah matter in room college account admit second teach list.
Listen door law., James Hernandez - similarbrittany85@example.com : 2023-11-25 17:41:09.393429+00:00, 1618.63, 426.13, {'genre': 'financial', 'pages': 382}: 5, Individual provide dark worker between control might actually apply board.
Yourself., William Ramos - lossayersjoyce@example.com : 2020-07-27 13:12:50.125815+00:00, 1594.35, 52.07, {'genre': 'world', 'pages': 436}: 3, Grow yeah again within forget color bar.
Sense scene power., Alexander Sanchez - militarysaraboone@example.com : 2020-05-31 01:28:59.924008+00:00, 4712.00, 66.57, {'genre': 'wind', 'pages': 410}: 5, Present check important them important make above.
Record great its., Jeffrey Burch - perautumn96@example.net : 2021-02-18 16:30:53.657978+00:00, 1976.47, 2.50, {'genre': 'ahead', 'pages': 437}: 3, On team writer hard edge value political future.
Attack pressure car., Andrew Ramirez - passkarlhardy@example.com : 2025-04-14 21:43:14.955402+00:00, 2031.81, 213.97, {'genre': 'weight', 'pages': 468}: 4, Need hand third miss range rate free claim stay measure them her either.
Turn thought., Billy Valentine - arrivelongvanessa@example.com : 2022-06-11 23:46:21.310719+00:00, 1203.91, 250.84, {'genre': 'behavior', 'pages': 122}: 4, Fight during turn matter career response offer sea meet move vote.
Republican special., Aimee Edwards - almostkelli67@example.org : 2023-09-28 04:47:54.153286+00:00, 935.13, 239.75, {'genre': 'space', 'pages': 293}: 4, Model sport pretty how build forward eat three.
Most member., Jessica Vaughn - audienceimontoya@example.net : 2020-07-05 02:10:17.238378+00:00, 2778.09, 444.16, {'genre': 'indicate', 'pages': 414}: 2, Institution camera foreign do they break fund.
Try successful red interesting., David Pearson - dealmichaelcrosby@example.org : 2022-07-26 05:04:29.021729+00:00, 2349.44, 15.60, {'genre': 'teach', 'pages': 447}: 3, Form power beat bank instead born.
Around police want., Ronald Hess - provekeithboyd@example.org : 2021-06-03 22:53:18.116466+00:00, 4334.61, 188.99, {'genre': 'could', 'pages': 378}: 1, Relate talk ball president daughter nothing might anything.
Budget., Amanda Snyder - tonightandreamann@example.com : 2021-02-26 23:45:12.512212+00:00, 3946.58, 6.65, {'genre': 'civil', 'pages': 497}: 2, Drug surface free owner so government pass everyone wall off them fall.
A decision including., Melissa Smith - paintingcampbelltony@example.org : 2023-04-30 17:06:11.931089+00:00, 1353.06, 354.56, {'genre': 'skill', 'pages': 258}: 5, Possible energy choose financial fall purpose prove detail.
Finish these late., Robert Rodriguez - costmartin81@example.org : 2022-03-23 13:11:20.344322+00:00, 1501.13, 448.78, {'genre': 'article', 'pages': 482}: 3, Should bag detail seem realize yet crime teacher page military building.
Cell risk him., Eddie Jones - dinnerlisa39@example.net : 2020-12-12 18:50:39.277172+00:00, 2567.46, 351.29, {'genre': 'still', 'pages': 235}: 4, Memory low consider yet thousand garden.
Let too far., Michael Washington - piecewilliamcurtis@example.org : 2021-05-26 13:57:38.761796+00:00, 3569.43, 298.70, {'genre': 'contain', 'pages': 428}: 3, American land feel space build far clearly somebody discover attorney ready project.
Improve office city certainly., Ashley Cox - standbstone@example.com : 2020-10-29 02:24:37.380551+00:00, 2042.32, 140.85, {'genre': 'food', 'pages': 113}: 5, Clearly likely former region performance kind according beat body job thought.
Art TV soldier bad., Gregory Johns - weightchristopher58@example.com : 2024-03-24 12:21:25.612422+00:00, 4690.55, 255.95, {'genre': 'owner', 'pages': 490}: 4, Tell hotel structure any professional read defense truth enter doctor rule.
Middle rich research., Holly Freeman - rockzberry@example.com : 2024-04-15 02:48:03.072250+00:00, 3996.92, 178.95, {'genre': 'past', 'pages': 185}: 3, Discuss find ball experience ago red quite employee meet own can last vote.
Easy., Sarah Sellers - nothingrobynvasquez@example.net : 2020-06-28 17:11:26.338210+00:00, 4019.14, 278.80, {'genre': 'likely', 'pages': 415}: 4, Base explain pass individual tax most future first head short image husband.
Until campaign., Susan Alvarez - footcynthiaallen@example.net : 2024-11-17 04:14:51.081878+00:00, 4041.79, 147.49, {'genre': 'time', 'pages': 239}: 3, Color quite plan source stay eat night check thought yard never artist hundred.
Middle fast billion., Tanner Flores - includingamanda70@example.com : 2022-08-20 11:14:50.138705+00:00, 616.06, 102.29, {'genre': 'explain', 'pages': 478}: 1, Hand enough what first hundred field current example story officer.
Ball reflect plan., Andrew Patterson - paybrandisanchez@example.com : 2024-10-03 02:45:59.039009+00:00, 3813.45, 28.34, {'genre': 'nation', 'pages': 290}: 2, Yard two too or usually TV color trial well move actually million.
List guess interview traditional., Erika Griffin - darkjoshuarojas@example.org : 2024-08-17 22:36:15.249511+00:00, 4948.21, 274.56, {'genre': 'risk', 'pages': 487}: 2, Anything receive suddenly fish find our event front.
Evidence try., Christopher Garner - throughkarenrobbins@example.org : 2022-01-11 14:40:58.049227+00:00, 2173.69, 117.08, {'genre': 'point', 'pages': 303}: 3, He hair rule theory energy local season.
Ok team social., Donna Odonnell - flylaura15@example.com : 2025-01-28 14:32:05.525324+00:00, 939.59, 151.98, {'genre': 'edge', 'pages': 390}: 2, Turn figure tend read system goal.
Floor bed land., David Casey - regiondickersonpamela@example.org : 2021-09-17 07:29:47.031686+00:00, 1173.55, 418.55, {'genre': 'day', 'pages': 101}: 1, Exist purpose name again involve Congress station blue foot beautiful citizen keep theory.
Strong occur., Justin Greer - wonderjeremy12@example.net : 2023-03-21 05:06:59.574505+00:00, 4183.10, 261.46, {'genre': 'near', 'pages': 262}: 3, Alone commercial me tax summer certainly opportunity decide lawyer represent ago participant western.
First., Matthew Edwards - whodmorton@example.org : 2020-01-30 00:29:55.039157+00:00, 1837.03, 308.44, {'genre': 'build', 'pages': 331}: 1, Movie money learn way expert production subject.
Have everyone best., Patricia Williams - sitegrantdale@example.net : 2021-02-12 13:23:39.762859+00:00, 3216.71, 277.96, {'genre': 'agree', 'pages': 413}: 4, Ability level onto spring break why others within test government still.
Factor no stock., Elizabeth Smith - useplee@example.net : 2023-06-05 16:46:45.233151+00:00, 2847.17, 289.51, {'genre': 'arrive', 'pages': 211}: 4, Tonight sign show station box will.
Resource some at until., Joshua Oneill - numberwhitney18@example.com : 2024-07-09 18:02:14.207258+00:00, 1026.96, 265.93, {'genre': 'model', 'pages': 454}: 2, Skin TV remember baby here stop recently above maybe gun action wind trial.
South rule perhaps., Kelly Wong - professorduncanzachary@example.net : 2024-04-10 22:56:10.240699+00:00, 4748.66, 352.71, {'genre': 'song', 'pages': 129}: 2, So something out themselves thing rate.
That administration., Jessica White - dataqjackson@example.org : 2023-07-21 13:04:06.398977+00:00, 2414.19, 257.64, {'genre': 'can', 'pages': 427}: 5, Oil four admit deal past much.

14. Найди все отзывы, у которых есть комментарий.
In [3]: list_reviews = Review.objects.exclude(comment='').exclude(comment__isnull=True)[:50]
   ...: for r in list_reviews:
   ...:     print(r)
   ...: 
'Eight without.' от: Donald Phillips, оценка: 1, коментарий: Nothing blood way modern by make medical positive never at work pull food.
'Star owner.' от: David Hicks, оценка: 1, коментарий: President sign administration speak especially out tough girl since until contain.
'Work also professional.' от: Laura Sims, оценка: 1, коментарий: Interview ahead point wish cup attorney heart budget lot.
'Visit start lead.' от: Catherine Houston, оценка: 1, коментарий: Old factor purpose report century pass institution after wonder may course.
'Year agree.' от: Anna Flores, оценка: 4, коментарий: Cost yard add figure investment ten surface impact citizen however.
'Involve tell for.' от: Elizabeth Harrington, оценка: 4, коментарий: Notice pattern administration practice national sister remember government institution answer president.
'Along next history.' от: Jonathan Hayes, оценка: 4, коментарий: Stay great smile raise body front challenge relate base sure grow.
'During friend floor.' от: Taylor Jones, оценка: 5, коментарий: Chance along child large dinner air girl.
'Number into.' от: William Kline, оценка: 3, коментарий: Charge and situation ok step success suddenly sport song despite soldier seem agency age.
'North it.' от: Melissa Smith, оценка: 1, коментарий: Cultural pay stage time beautiful young through today full receive class view action.
'Last believe help.' от: Jacob Decker, оценка: 5, коментарий: Top down account finish memory front sometimes technology.
'Beyond either reach.' от: Anthony Wright, оценка: 3, коментарий: Above spend get defense skin travel keep finish yard young.
'At office.' от: Jaclyn Smith, оценка: 2, коментарий: Bit style real rather break particular along.
'Bag rich marriage.' от: Angela Fox, оценка: 5, коментарий: Part education prevent worker name find support only what agent.
'Certain main dark.' от: Monica Hardin, оценка: 1, коментарий: Reflect ability street hour process begin question yes let food commercial perhaps piece.
'Fish want main.' от: Craig Gillespie, оценка: 5, коментарий: Moment chair executive design such important raise difficult.
'Individual important laugh.' от: Brandi Robinson, оценка: 1, коментарий: Require leave manager yeah matter in room college account admit second teach list.
'Listen door law.' от: James Hernandez, оценка: 5, коментарий: Individual provide dark worker between control might actually apply board.
'Yourself.' от: William Ramos, оценка: 3, коментарий: Grow yeah again within forget color bar.
'Sense scene power.' от: Alexander Sanchez, оценка: 5, коментарий: Present check important them important make above.
'Record great its.' от: Jeffrey Burch, оценка: 3, коментарий: On team writer hard edge value political future.
'Attack pressure car.' от: Andrew Ramirez, оценка: 4, коментарий: Need hand third miss range rate free claim stay measure them her either.
'Turn thought.' от: Billy Valentine, оценка: 4, коментарий: Fight during turn matter career response offer sea meet move vote.
'Republican special.' от: Aimee Edwards, оценка: 4, коментарий: Model sport pretty how build forward eat three.
'Most member.' от: Jessica Vaughn, оценка: 2, коментарий: Institution camera foreign do they break fund.
'Try successful red interesting.' от: David Pearson, оценка: 3, коментарий: Form power beat bank instead born.
'Around police want.' от: Ronald Hess, оценка: 1, коментарий: Relate talk ball president daughter nothing might anything.
'Budget.' от: Amanda Snyder, оценка: 2, коментарий: Drug surface free owner so government pass everyone wall off them fall.
'A decision including.' от: Melissa Smith, оценка: 5, коментарий: Possible energy choose financial fall purpose prove detail.
'Finish these late.' от: Robert Rodriguez, оценка: 3, коментарий: Should bag detail seem realize yet crime teacher page military building.
'Cell risk him.' от: Eddie Jones, оценка: 4, коментарий: Memory low consider yet thousand garden.
'Let too far.' от: Michael Washington, оценка: 3, коментарий: American land feel space build far clearly somebody discover attorney ready project.
'Improve office city certainly.' от: Ashley Cox, оценка: 5, коментарий: Clearly likely former region performance kind according beat body job thought.
'Art TV soldier bad.' от: Gregory Johns, оценка: 4, коментарий: Tell hotel structure any professional read defense truth enter doctor rule.
'Middle rich research.' от: Holly Freeman, оценка: 3, коментарий: Discuss find ball experience ago red quite employee meet own can last vote.
'Easy.' от: Sarah Sellers, оценка: 4, коментарий: Base explain pass individual tax most future first head short image husband.
'Until campaign.' от: Susan Alvarez, оценка: 3, коментарий: Color quite plan source stay eat night check thought yard never artist hundred.
'Middle fast billion.' от: Tanner Flores, оценка: 1, коментарий: Hand enough what first hundred field current example story officer.
'Ball reflect plan.' от: Andrew Patterson, оценка: 2, коментарий: Yard two too or usually TV color trial well move actually million.
'List guess interview traditional.' от: Erika Griffin, оценка: 2, коментарий: Anything receive suddenly fish find our event front.
'Evidence try.' от: Christopher Garner, оценка: 3, коментарий: He hair rule theory energy local season.
'Ok team social.' от: Donna Odonnell, оценка: 2, коментарий: Turn figure tend read system goal.
'Floor bed land.' от: David Casey, оценка: 1, коментарий: Exist purpose name again involve Congress station blue foot beautiful citizen keep theory.
'Strong occur.' от: Justin Greer, оценка: 3, коментарий: Alone commercial me tax summer certainly opportunity decide lawyer represent ago participant western.
'First.' от: Matthew Edwards, оценка: 1, коментарий: Movie money learn way expert production subject.
'Have everyone best.' от: Patricia Williams, оценка: 4, коментарий: Ability level onto spring break why others within test government still.
'Factor no stock.' от: Elizabeth Smith, оценка: 4, коментарий: Tonight sign show station box will.
'Resource some at until.' от: Joshua Oneill, оценка: 2, коментарий: Skin TV remember baby here stop recently above maybe gun action wind trial.
'South rule perhaps.' от: Kelly Wong, оценка: 2, коментарий: So something out themselves thing rate.
'That administration.' от: Jessica White, оценка: 5, коментарий: Oil four admit deal past much.

### IN и Range
15. Найди авторов с идентификаторами 1, 3 и 5.
In [12]: list_authors = Author.objects.filter(pk__in=[2001, 2003, 2005])
In [13]: for a in list_authors:
    ...:     print(a)
    ...: 
Richard Harrington - sharetuckeromar@example.net
Douglas Li - smilexjuarez@example.org
Denise Lopez - politicalstephanie92@example.net
  
16. Найди книги, опубликованные с 1 января по 31 декабря 2023 года.
In [49]: list_books = Book.objects.filter(published_date__year=2023)[:50]
In [50]: for b in list_books:
    ...:     print(b)
    ...: 
'Meeting letter mean.', от: Angela Escobar - certainlyhebertrobert@example.com, опубликовано: 2023-02-22 00:37:31.716172+00:00, цена:3344.98,скидка: 312.02, доп данные:{'genre': 'affect', 'pages': 148}
'Meeting environment.', от: Donald Zhang - servemarylewis@example.net, опубликовано: 2023-06-16 10:05:45.086483+00:00, цена:1168.09,скидка: 357.66, доп данные:{'genre': 'from', 'pages': 131}
'Fear.', от: Brandon Mcknight - eventheresa60@example.org, опубликовано: 2023-11-25 02:28:17.794569+00:00, цена:2339.26,скидка: 88.25, доп данные:{'genre': 'writer', 'pages': 490}
'Instead thank.', от: Nicole Jimenez - firstchristopher00@example.com, опубликовано: 2023-08-26 03:21:51.787934+00:00, цена:3845.65,скидка: 341.32, доп данные:{'genre': 'popular', 'pages': 174}
'Much myself born sometimes.', от: Jeffrey Taylor - PMamarquez@example.org, опубликовано: 2023-10-05 14:36:01.704642+00:00, цена:903.83,скидка: 1.06, доп данные:{'genre': 'short', 'pages': 121}
'Protect drug.', от: Angela Shaw - weekohumphrey@example.com, опубликовано: 2023-04-10 05:58:22.841906+00:00, цена:596.32,скидка: 282.24, доп данные:{'genre': 'benefit', 'pages': 175}
'Perform.', от: Andrea Arnold - cityrhill@example.org, опубликовано: 2023-02-04 02:14:07.528152+00:00, цена:1222.16,скидка: 133.04, доп данные:{'genre': 'reality', 'pages': 395}
'Sell where.', от: Edward Williams - structuresmithhannah@example.org, опубликовано: 2023-01-05 23:43:20.531107+00:00, цена:2834.86,скидка: 422.92, доп данные:{'genre': 'culture', 'pages': 148}
'Forget picture yard.', от: Robert Holmes - specialharrisjamie@example.com, опубликовано: 2023-01-12 10:16:55.217300+00:00, цена:3675.25,скидка: 258.50, доп данные:{'genre': 'interesting', 'pages': 281}
'Bad read north.', от: Matthew Kane - healthmcdanieldestiny@example.org, опубликовано: 2023-07-29 18:32:56.732831+00:00, цена:1393.40,скидка: 372.70, доп данные:{'genre': 'able', 'pages': 149}
'Worry conference.', от: Daniel Stone - magazinebenjaminsaunders@example.com, опубликовано: 2023-04-20 15:10:52.078236+00:00, цена:1284.96,скидка: 286.58, доп данные:{'genre': 'drive', 'pages': 329}
'Movie arrive.', от: George Cantu - calldsmith@example.com, опубликовано: 2023-01-05 20:53:18.709620+00:00, цена:1038.03,скидка: 292.70, доп данные:{'genre': 'produce', 'pages': 154}
'Movie improve course.', от: Jamie Ramirez - catchjohnsonelizabeth@example.org, опубликовано: 2023-01-13 13:52:15.091417+00:00, цена:3350.22,скидка: 279.63, доп данные:{'genre': 'level', 'pages': 421}
'Thus rise.', от: Peter Brewer - rangehernandezdavid@example.net, опубликовано: 2023-05-20 04:24:35.402838+00:00, цена:3444.06,скидка: 104.08, доп данные:{'genre': 'really', 'pages': 380}
'Century explain rich.', от: Lindsey Conrad - acceptegarcia@example.org, опубликовано: 2023-05-07 09:52:14.338361+00:00, цена:3657.27,скидка: 147.50, доп данные:{'genre': 'analysis', 'pages': 242}
'Painting produce me.', от: Patricia Williams - sitegrantdale@example.net, опубликовано: 2023-01-02 06:27:04.610348+00:00, цена:2761.79,скидка: 215.32, доп данные:{'genre': 'peace', 'pages': 477}
'Drop public attorney.', от: Craig Hill - girlmooreamanda@example.net, опубликовано: 2023-07-01 10:20:16.639476+00:00, цена:3520.43,скидка: 412.59, доп данные:{'genre': 'together', 'pages': 414}
'Job raise.', от: Dave Brown - challengejakehayes@example.org, опубликовано: 2023-01-15 21:34:35.402212+00:00, цена:3037.94,скидка: 364.47, доп данные:{'genre': 'relate', 'pages': 410}
'Keep Democrat.', от: Eric Reed - seriousbmayer@example.org, опубликовано: 2023-06-08 14:45:18.123302+00:00, цена:3426.92,скидка: 32.49, доп данные:{'genre': 'whom', 'pages': 215}
'Beyond fast site.', от: Richard Skinner - kindjillcollins@example.org, опубликовано: 2023-12-29 19:49:06.734682+00:00, цена:3937.52,скидка: 31.67, доп данные:{'genre': 'maybe', 'pages': 458}
'Some increase while.', от: Theodore Smith - throughdonnadecker@example.net, опубликовано: 2023-01-13 19:12:57.264969+00:00, цена:1174.86,скидка: 204.52, доп данные:{'genre': 'experience', 'pages': 383}
'Republican son center.', от: Jean Chase - mediaschwartzmichelle@example.com, опубликовано: 2023-11-13 09:46:21.276641+00:00, цена:4257.00,скидка: 11.76, доп данные:{'genre': 'since', 'pages': 495}
'Base skill.', от: Christopher Rogers - billamberjones@example.com, опубликовано: 2023-04-08 11:38:28.491977+00:00, цена:3982.20,скидка: 141.96, доп данные:{'genre': 'successful', 'pages': 417}
'Audience house she.', от: Eric Green - dealggarcia@example.org, опубликовано: 2023-12-14 02:45:50.553870+00:00, цена:795.54,скидка: 265.11, доп данные:{'genre': 'conference', 'pages': 194}
'New through break.', от: Denise Lopez - politicalstephanie92@example.net, опубликовано: 2023-09-09 18:33:34.410102+00:00, цена:4545.76,скидка: 251.44, доп данные:{'genre': 'significant', 'pages': 346}
'Matter us.', от: Angela Roberts - itsbrandondavis@example.org, опубликовано: 2023-07-31 06:44:35.348142+00:00, цена:3473.66,скидка: 354.53, доп данные:{'genre': 'however', 'pages': 261}
'General check.', от: Yolanda Phillips - thesewoodwardsusan@example.net, опубликовано: 2023-05-26 20:20:17.333421+00:00, цена:3988.15,скидка: 223.85, доп данные:{'genre': 'address', 'pages': 256}
'Other night.', от: Vanessa Brown - threethomasdavid@example.com, опубликовано: 2023-03-20 20:14:35.282135+00:00, цена:4348.36,скидка: 377.88, доп данные:{'genre': 'despite', 'pages': 484}
'Store young.', от: Ethan Williams - lotdavid74@example.net, опубликовано: 2023-01-18 06:41:49.419778+00:00, цена:2200.37,скидка: 402.35, доп данные:{'genre': 'story', 'pages': 109}
'Watch truth quality together.', от: Susan Green - smallsarahrichards@example.com, опубликовано: 2023-11-07 17:17:57.825839+00:00, цена:2328.27,скидка: 347.94, доп данные:{'genre': 'medical', 'pages': 318}
'Know.', от: Jennifer Krueger - linejason82@example.com, опубликовано: 2023-10-18 09:38:18.808585+00:00, цена:3748.96,скидка: 437.03, доп данные:{'genre': 'stand', 'pages': 195}
'Newspaper over natural.', от: Patricia Alvarez - hardcarmenbush@example.org, опубликовано: 2023-03-06 22:33:07.226953+00:00, цена:3964.64,скидка: 101.02, доп данные:{'genre': 'institution', 'pages': 378}
'Good tax Republican.', от: Vincent Harper - specificamber49@example.com, опубликовано: 2023-03-14 13:49:27.544406+00:00, цена:2548.53,скидка: 281.82, доп данные:{'genre': 'send', 'pages': 320}
'Teacher.', от: Danielle Wells - generalybell@example.net, опубликовано: 2023-02-10 02:11:23.664300+00:00, цена:3105.97,скидка: 76.82, доп данные:{'genre': 'community', 'pages': 237}
'Mother drug.', от: Philip Sanders - comparethompsoncathy@example.org, опубликовано: 2023-03-25 19:58:57.462626+00:00, цена:2316.13,скидка: 146.21, доп данные:{'genre': 'marriage', 'pages': 281}
'Forget trouble Democrat.', от: Elizabeth Branch - oilkstephens@example.org, опубликовано: 2023-12-17 01:17:39.607389+00:00, цена:4090.58,скидка: 284.38, доп данные:{'genre': 'cover', 'pages': 453}
'Worry term.', от: Angela Williams - wayokramer@example.com, опубликовано: 2023-02-28 10:30:59.593347+00:00, цена:3568.71,скидка: 97.04, доп данные:{'genre': 'computer', 'pages': 239}
'Edge image recent.', от: Joan Johnson - containkelleyjohn@example.com, опубликовано: 2023-10-03 21:11:14.705039+00:00, цена:1987.52,скидка: 147.11, доп данные:{'genre': 'quality', 'pages': 307}
'More sport cost.', от: Patricia Alvarez - hardcarmenbush@example.org, опубликовано: 2023-11-23 16:17:28.552177+00:00, цена:4018.59,скидка: 216.74, доп данные:{'genre': 'reflect', 'pages': 441}
'Sit six.', от: Ashley Miller - musichannah86@example.com, опубликовано: 2023-01-14 01:05:56.211150+00:00, цена:1123.57,скидка: 188.84, доп данные:{'genre': 'knowledge', 'pages': 228}
'Son project.', от: Adriana Moore - spacewhicks@example.org, опубликовано: 2023-01-23 13:52:07.260052+00:00, цена:864.62,скидка: 331.68, доп данные:{'genre': 'nice', 'pages': 321}
'Difference available.', от: Russell Thompson - addbaileyorozco@example.net, опубликовано: 2023-02-13 06:10:01.510798+00:00, цена:1799.44,скидка: 114.77, доп данные:{'genre': 'value', 'pages': 409}
'Main however.', от: Kathleen Macdonald - firstmartinmatthew@example.org, опубликовано: 2023-04-23 01:41:48.282363+00:00, цена:658.27,скидка: 17.96, доп данные:{'genre': 'keep', 'pages': 156}
'May ready really soldier.', от: Jennifer Chan - attentionmccoykevin@example.net, опубликовано: 2023-03-03 08:13:27.946852+00:00, цена:4997.83,скидка: 141.97, доп данные:{'genre': 'learn', 'pages': 398}
'Prove wear friend.', от: Sarah Montes - truthheather87@example.net, опубликовано: 2023-07-15 06:00:26.428263+00:00, цена:2502.46,скидка: 68.94, доп данные:{'genre': 'his', 'pages': 240}
'As result choose.', от: Timothy Bowman - joinlisa42@example.com, опубликовано: 2023-06-15 16:11:59.781881+00:00, цена:2422.70,скидка: 73.72, доп данные:{'genre': 'idea', 'pages': 486}
'Miss TV area central.', от: Wyatt Carroll - feelgloria29@example.com, опубликовано: 2023-05-11 00:29:36.678199+00:00, цена:3755.97,скидка: 351.14, доп данные:{'genre': 'how', 'pages': 125}
'Hair enjoy.', от: Michael Brooks - recentchristopher50@example.org, опубликовано: 2023-04-27 07:05:32.007614+00:00, цена:4028.65,скидка: 389.82, доп данные:{'genre': 'keep', 'pages': 450}
'Out between clear.', от: Morgan Andrade - significantallisonhernandez@example.com, опубликовано: 2023-10-03 05:17:56.939869+00:00, цена:663.66,скидка: 440.85, доп данные:{'genre': 'writer', 'pages': 418}
'Involve difficult of.', от: Christian Fry - thoughtjonathancarr@example.net, опубликовано: 2023-10-03 02:02:36.512368+00:00, цена:3081.42,скидка: 13.27, доп данные:{'genre': 'shoulder', 'pages': 422}

### Регулярные выражения
17. Найди книги, название которых начинается со слова «Python».  
In [31]: list_books = Book.objects.filter(title__startswith='Python')
In [32]: list_books
Out[32]: <QuerySet []>
    
18. Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр). 
In [33]: list_authors = Author.objects.filter(last_name__istartswith='Mc')
In [35]: for a in list_authors:
    ...:     print(a)
    ...: 
Brianna Mccoy - majorwesley77@example.com
Raymond Mccormick - firestoneblake@example.com
Kaitlyn Mccall - shoulderharperjoseph@example.com
Kari Mckenzie - significantlaura99@example.com
Kenneth Mcneil - knowledgeegrant@example.net
Scott Mcclain - fightfgallegos@example.com
Ryan Mcclain - storyzmoon@example.net
Jorge Mcdowell - westernmendozaandrew@example.org
Cody Mcdonald - situationrebecca39@example.com
Eric Mcbride - whilecatherinefoster@example.com
Brandon Mcknight - eventheresa60@example.org
Brittany Mcfarland - internationaluporter@example.net
Cory Mccann - protectwthomas@example.com

### Даты и время
19. Найди книги, опубликованные в 2024 году. 
In [55]: list_books = Book.objects.filter(published_date__year=2024)[:25]
In [56]: for b in list_books:
    ...:     print(b)
    ...: 
'Break nation.', от: Bonnie Hess - alonekimberlywilliams@example.com, опубликовано: 2024-07-30 21:59:22.048699+00:00, цена:855.60,скидка: 344.45, доп данные:{'genre': 'theory', 'pages': 212}
'Beyond respond consider.', от: Harold Wagner - nearlyahenry@example.org, опубликовано: 2024-02-24 20:06:18.649125+00:00, цена:4567.98,скидка: 334.74, доп данные:{'genre': 'unit', 'pages': 468}
'Film local technology somebody.', от: Timothy Allen - anythingkelleyjessica@example.com, опубликовано: 2024-04-16 21:34:13.559933+00:00, цена:532.95,скидка: 437.56, доп данные:{'genre': 'serve', 'pages': 346}
'We current popular.', от: Michele Williamson - strongjosephjones@example.org, опубликовано: 2024-08-25 13:31:12.192678+00:00, цена:3798.76,скидка: 407.86, доп данные:{'genre': 'second', 'pages': 267}
'Ask TV.', от: Christopher Rogers - billamberjones@example.com, опубликовано: 2024-10-10 20:23:04.896218+00:00, цена:2844.66,скидка: 320.46, доп данные:{'genre': 'near', 'pages': 451}
'Fire suffer around radio.', от: Chad Dunn - investmenturamos@example.net, опубликовано: 2024-09-15 19:47:58.925880+00:00, цена:2818.96,скидка: 375.67, доп данные:{'genre': 'mother', 'pages': 259}
'Season start.', от: Robert Graves - sixmichelle76@example.com, опубликовано: 2024-09-13 06:46:21.382140+00:00, цена:1403.68,скидка: 430.87, доп данные:{'genre': 'kitchen', 'pages': 164}
'Kitchen material lose.', от: Denise Hall - thosejohnreyes@example.org, опубликовано: 2024-08-20 15:11:40.577817+00:00, цена:4226.24,скидка: 431.06, доп данные:{'genre': 'reality', 'pages': 311}
'Author try charge.', от: John Smith - statementjackhardy@example.org, опубликовано: 2024-01-17 17:29:27.206612+00:00, цена:4769.70,скидка: 370.92, доп данные:{'genre': 'it', 'pages': 293}
'Experience I democratic.', от: Jonathan Silva - musicstonejeffery@example.org, опубликовано: 2024-11-16 16:20:22.888509+00:00, цена:4584.24,скидка: 370.41, доп данные:{'genre': 'hand', 'pages': 449}
'Participant environmental.', от: Natalie Owens - churchxcollins@example.org, опубликовано: 2024-12-20 07:04:17.914972+00:00, цена:3940.56,скидка: 106.55, доп данные:{'genre': 'after', 'pages': 392}
'Marriage series forward.', от: Andre Ellison - betterpshaffer@example.org, опубликовано: 2024-02-26 02:23:30.642237+00:00, цена:4508.86,скидка: 342.63, доп данные:{'genre': 'sure', 'pages': 399}
'Enjoy I morning.', от: Christopher Green - maybeshawnalucas@example.com, опубликовано: 2024-01-21 06:07:28.472442+00:00, цена:1012.44,скидка: 38.99, доп данные:{'genre': 'month', 'pages': 174}
'Pm artist season.', от: Ashley Torres - begoodmanjohn@example.org, опубликовано: 2024-07-21 03:42:51.277729+00:00, цена:4234.48,скидка: 209.09, доп данные:{'genre': 'surface', 'pages': 417}
'Whether training campaign.', от: Autumn Hicks - closemorrisdominique@example.net, опубликовано: 2024-03-17 00:23:45.268717+00:00, цена:2108.65,скидка: 9.07, доп данные:{'genre': 'which', 'pages': 222}
'System beyond special garden.', от: Alicia Dunn - theoryysingleton@example.org, опубликовано: 2024-01-19 09:58:22.640942+00:00, цена:4373.88,скидка: 101.79, доп данные:{'genre': 'management', 'pages': 298}
'Gas wait.', от: Kelly King - peoplelcampbell@example.com, опубликовано: 2024-01-13 22:14:01.107967+00:00, цена:2589.51,скидка: 420.43, доп данные:{'genre': 'too', 'pages': 119}
'Go house.', от: Ralph Thomas - hospitalmendezjames@example.net, опубликовано: 2024-04-24 03:54:07.436451+00:00, цена:3360.12,скидка: 43.53, доп данные:{'genre': 'case', 'pages': 402}
'Discover everyone trip.', от: Joseph Jones - carryhudsonjeremiah@example.com, опубликовано: 2024-10-02 06:02:45.042029+00:00, цена:1076.52,скидка: 176.47, доп данные:{'genre': 'skill', 'pages': 479}
'Drive central.', от: Morgan Alvarez - schooltanya26@example.org, опубликовано: 2024-09-02 07:05:13.228538+00:00, цена:1695.82,скидка: 327.06, доп данные:{'genre': 'wrong', 'pages': 442}
'World.', от: Kenneth Mcneil - knowledgeegrant@example.net, опубликовано: 2024-07-15 02:50:08.923859+00:00, цена:727.11,скидка: 112.60, доп данные:{'genre': 'poor', 'pages': 138}
'Middle.', от: Jason Parks - secondrobinsonvictor@example.com, опубликовано: 2024-04-02 07:44:04.908302+00:00, цена:2075.12,скидка: 317.24, доп данные:{'genre': 'onto', 'pages': 361}
'Account drive finish.', от: Danielle Wood - enjoythomasgarner@example.com, опубликовано: 2024-11-09 19:29:57.659662+00:00, цена:3807.63,скидка: 76.96, доп данные:{'genre': 'since', 'pages': 380}
'Skill they.', от: Aaron Morales - institutionlaurenallison@example.net, опубликовано: 2024-10-17 20:06:52.000042+00:00, цена:2183.62,скидка: 279.25, доп данные:{'genre': 'benefit', 'pages': 286}
'Bad management large thousand.', от: Andrew Allison - memoryxavier95@example.com, опубликовано: 2024-12-11 01:17:38.324738+00:00, цена:2379.79,скидка: 310.96, доп данные:{'genre': 'half', 'pages': 197}
   
20. Найди книги, опубликованные в июне.  
In [60]: list_books = Book.objects.filter(published_date__month=6)[:25]
In [61]: for b in list_books:
    ...:     print(b)
    ...: 
'Professional keep.', от: Victor Kelly - memorymadisonmoore@example.com, опубликовано: 2020-06-28 22:49:55.351064+00:00, цена:1295.24,скидка: 395.76, доп данные:{'genre': 'player', 'pages': 132}
'Meeting environment.', от: Donald Zhang - servemarylewis@example.net, опубликовано: 2023-06-16 10:05:45.086483+00:00, цена:1168.09,скидка: 357.66, доп данные:{'genre': 'from', 'pages': 131}
'To seem live.', от: Kelly Wong - professorduncanzachary@example.net, опубликовано: 2025-06-15 18:10:38.601416+00:00, цена:3554.58,скидка: 289.80, доп данные:{'genre': 'opportunity', 'pages': 451}
'Personal.', от: Kelly Hardy - leastgarciaryan@example.net, опубликовано: 2020-06-14 21:58:05.944401+00:00, цена:4295.98,скидка: 161.00, доп данные:{'genre': 'store', 'pages': 340}
'Cut hotel.', от: Jonathan Elliott - Mrdanielwright@example.org, опубликовано: 2021-06-11 04:59:18.930929+00:00, цена:1464.49,скидка: 243.78, доп данные:{'genre': 'yourself', 'pages': 366}
'Power personal evidence.', от: Amber Crawford - dogdaniel39@example.com, опубликовано: 2022-06-19 16:45:21.558637+00:00, цена:3169.35,скидка: 253.44, доп данные:{'genre': 'population', 'pages': 248}
'Especially finally.', от: Victoria Bush - thoseyorkemily@example.org, опубликовано: 2025-06-09 07:52:01.523347+00:00, цена:877.47,скидка: 418.10, доп данные:{'genre': 'cut', 'pages': 353}
'Process few resource.', от: Kenneth Hart - whomjoseph81@example.com, опубликовано: 2022-06-23 10:34:50.001297+00:00, цена:2234.05,скидка: 330.23, доп данные:{'genre': 'idea', 'pages': 137}
'Interview dinner cause.', от: Holly Lopez - thinkajackson@example.org, опубликовано: 2025-06-10 19:11:00.930888+00:00, цена:2035.45,скидка: 296.52, доп данные:{'genre': 'throw', 'pages': 160}
'Keep Democrat.', от: Eric Reed - seriousbmayer@example.org, опубликовано: 2023-06-08 14:45:18.123302+00:00, цена:3426.92,скидка: 32.49, доп данные:{'genre': 'whom', 'pages': 215}
'Four career.', от: Vanessa Parks - orkenneth79@example.org, опубликовано: 2022-06-11 01:13:01.212683+00:00, цена:3487.17,скидка: 433.11, доп данные:{'genre': 'good', 'pages': 470}
'Win case hear.', от: Hannah Moore - dinnermatthew74@example.com, опубликовано: 2025-06-02 01:02:56.299854+00:00, цена:3185.11,скидка: 255.26, доп данные:{'genre': 'shake', 'pages': 210}
'Large manage among television.', от: Margaret Sawyer - viewjoseph07@example.org, опубликовано: 2020-06-04 01:54:32.411355+00:00, цена:1839.15,скидка: 290.33, доп данные:{'genre': 'range', 'pages': 202}
'Down sell.', от: Sandra Lowe - theygeorgediana@example.com, опубликовано: 2025-06-07 17:52:50.345073+00:00, цена:776.39,скидка: 335.41, доп данные:{'genre': 'marriage', 'pages': 277}
'Our image dark.', от: Sandra Scott - pricehwilson@example.org, опубликовано: 2024-06-15 22:27:32.119144+00:00, цена:2225.83,скидка: 301.40, доп данные:{'genre': 'red', 'pages': 230}
'Shake us.', от: Clayton Davis - nextdanielsjimmy@example.org, опубликовано: 2022-06-17 16:09:18.537354+00:00, цена:4639.21,скидка: 188.19, доп данные:{'genre': 'certain', 'pages': 250}
'Majority author record.', от: Larry Summers - whyflucas@example.org, опубликовано: 2020-06-20 10:53:53.659738+00:00, цена:4141.51,скидка: 390.38, доп данные:{'genre': 'party', 'pages': 485}
'Outside occur ten.', от: Melody Norris - manqstewart@example.com, опубликовано: 2025-06-11 19:21:58.358936+00:00, цена:1157.71,скидка: 298.67, доп данные:{'genre': 'finish', 'pages': 110}
'Tree edge check.', от: Kelly Cooper - guessnicole47@example.org, опубликовано: 2022-06-27 00:05:44.767771+00:00, цена:4533.97,скидка: 353.79, доп данные:{'genre': 'piece', 'pages': 431}
'Ready leader sense about.', от: Jeffrey Sampson - leadjonathanfriedman@example.org, опубликовано: 2021-06-17 00:16:18.168746+00:00, цена:858.05,скидка: 270.11, доп данные:{'genre': 'general', 'pages': 255}
'As result choose.', от: Timothy Bowman - joinlisa42@example.com, опубликовано: 2023-06-15 16:11:59.781881+00:00, цена:2422.70,скидка: 73.72, доп данные:{'genre': 'idea', 'pages': 486}
'Some which feeling.', от: Tyrone Lloyd - particularereyes@example.org, опубликовано: 2022-06-23 23:03:32.237327+00:00, цена:1726.10,скидка: 342.90, доп данные:{'genre': 'report', 'pages': 270}
'Hair what else.', от: Daniel Harmon - largezalvarado@example.net, опубликовано: 2020-06-06 17:21:00.137983+00:00, цена:2189.65,скидка: 425.26, доп данные:{'genre': 'sometimes', 'pages': 495}
'Performance hear.', от: Tiffany Daugherty - accordingbryantedwin@example.org, опубликовано: 2025-06-09 08:11:49.156363+00:00, цена:3559.97,скидка: 116.61, доп данные:{'genre': 'form', 'pages': 312}
'Plan compare.', от: Scott Mcclain - fightfgallegos@example.com, опубликовано: 2023-06-16 18:26:36.813741+00:00, цена:4192.09,скидка: 71.89, доп данные:{'genre': 'each', 'pages': 390}
     
21. Найди отзывы, оставленные 11-го числа любого месяца.  
In [65]: list_reviews = Review.objects.filter(created_at__day=11)[:25]
In [66]: list_reviews
Out[66]: <QuerySet []>
       
22. Найди книги, опубликованные на 23-й неделе года.  
In [71]: list_books = Book.objects.filter(published_date__week=23)[:25]
In [72]: for b in list_books:
    ...:     print(b)
    ...: 
'Cut hotel.', от: Jonathan Elliott - Mrdanielwright@example.org, опубликовано: 2021-06-11 04:59:18.930929+00:00, цена:1464.49,скидка: 243.78, доп данные:{'genre': 'yourself', 'pages': 366}
'Keep Democrat.', от: Eric Reed - seriousbmayer@example.org, опубликовано: 2023-06-08 14:45:18.123302+00:00, цена:3426.92,скидка: 32.49, доп данные:{'genre': 'whom', 'pages': 215}
'Four career.', от: Vanessa Parks - orkenneth79@example.org, опубликовано: 2022-06-11 01:13:01.212683+00:00, цена:3487.17,скидка: 433.11, доп данные:{'genre': 'good', 'pages': 470}
'Win case hear.', от: Hannah Moore - dinnermatthew74@example.com, опубликовано: 2025-06-02 01:02:56.299854+00:00, цена:3185.11,скидка: 255.26, доп данные:{'genre': 'shake', 'pages': 210}
'Large manage among television.', от: Margaret Sawyer - viewjoseph07@example.org, опубликовано: 2020-06-04 01:54:32.411355+00:00, цена:1839.15,скидка: 290.33, доп данные:{'genre': 'range', 'pages': 202}
'Down sell.', от: Sandra Lowe - theygeorgediana@example.com, опубликовано: 2025-06-07 17:52:50.345073+00:00, цена:776.39,скидка: 335.41, доп данные:{'genre': 'marriage', 'pages': 277}
'Hair what else.', от: Daniel Harmon - largezalvarado@example.net, опубликовано: 2020-06-06 17:21:00.137983+00:00, цена:2189.65,скидка: 425.26, доп данные:{'genre': 'sometimes', 'pages': 495}
'Sound identify.', от: Martin Hansen - heartpattersongarrett@example.net, опубликовано: 2021-06-10 02:00:19.020613+00:00, цена:4018.28,скидка: 112.95, доп данные:{'genre': 'theory', 'pages': 126}
'Somebody box.', от: John Romero - voicerogersmark@example.org, опубликовано: 2024-06-03 00:14:33.945341+00:00, цена:544.93,скидка: 219.33, доп данные:{'genre': 'party', 'pages': 296}
'South time first.', от: Tina Smith - modeldianehall@example.com, опубликовано: 2023-06-06 01:26:10.376853+00:00, цена:4708.16,скидка: 220.66, доп данные:{'genre': 'dark', 'pages': 132}
'Budget owner.', от: James Johnson - veryaustin66@example.com, опубликовано: 2024-06-04 00:25:35.058920+00:00, цена:3994.65,скидка: 108.35, доп данные:{'genre': 'PM', 'pages': 192}
'Sing look.', от: Drew Myers - theorywilliamstammy@example.org, опубликовано: 2024-06-03 13:26:55.993623+00:00, цена:2474.47,скидка: 220.56, доп данные:{'genre': 'nation', 'pages': 113}
'Tax hot.', от: Monica Oliver - morningmatthewowens@example.org, опубликовано: 2023-06-07 14:12:20.921483+00:00, цена:504.96,скидка: 436.72, доп данные:{'genre': 'floor', 'pages': 190}
'Able role.', от: David Richardson - spendjessicagrimes@example.net, опубликовано: 2020-06-05 10:21:56.193823+00:00, цена:1229.86,скидка: 422.80, доп данные:{'genre': 'yes', 'pages': 139}
'Partner over.', от: Christina Harrington - nearifisher@example.com, опубликовано: 2023-06-08 13:49:43.640975+00:00, цена:1616.20,скидка: 266.41, доп данные:{'genre': 'yourself', 'pages': 123}
'Little hold fact author.', от: Monica Oliver - morningmatthewowens@example.org, опубликовано: 2022-06-10 00:13:50.041634+00:00, цена:1433.12,скидка: 113.90, доп данные:{'genre': 'eight', 'pages': 126}
'Film.', от: Lori Ramirez - existudavis@example.net, опубликовано: 2021-06-08 19:02:45.233608+00:00, цена:2178.03,скидка: 111.70, доп данные:{'genre': 'those', 'pages': 320}
'When feel alone.', от: Nicole White - normonica92@example.org, опубликовано: 2020-06-01 07:54:16.868710+00:00, цена:4411.22,скидка: 300.31, доп данные:{'genre': 'almost', 'pages': 185}
'After strategy indeed.', от: Jennifer Wilson - losemooneyrichard@example.net, опубликовано: 2025-06-08 13:40:39.797442+00:00, цена:2030.95,скидка: 243.74, доп данные:{'genre': 'president', 'pages': 425}
'North it.', от: Melissa Smith - paintingcampbelltony@example.org, опубликовано: 2025-06-04 23:12:46.578654+00:00, цена:3031.29,скидка: 176.94, доп данные:{'genre': 'teach', 'pages': 343}
'Gas about.', от: Steven Thompson - questionjocelyngoodman@example.org, опубликовано: 2020-06-01 05:43:05.395164+00:00, цена:4132.25,скидка: 382.10, доп данные:{'genre': 'true', 'pages': 385}
'Brother weight.', от: Kelly Barnett - darkgraceramirez@example.org, опубликовано: 2024-06-06 06:52:13.476446+00:00, цена:2650.46,скидка: 244.22, доп данные:{'genre': 'write', 'pages': 286}
'Threat clearly treat.', от: Deborah Turner - readcody46@example.net, опубликовано: 2021-06-09 17:28:11.073110+00:00, цена:1001.29,скидка: 335.23, доп данные:{'genre': 'return', 'pages': 208}
'Money assume worker.', от: Darlene Shaw - citytamara01@example.org, опубликовано: 2025-06-07 11:57:14.785249+00:00, цена:3035.41,скидка: 448.75, доп данные:{'genre': 'drop', 'pages': 189}
'Key language buy.', от: Melinda Frey - jobtiffany38@example.net, опубликовано: 2022-06-08 07:23:16.918579+00:00, цена:918.19,скидка: 70.95, доп данные:{'genre': 'feel', 'pages': 114}

23. Найди отзывы, оставленные во вторник.  
In [74]: list_reviews = Review.objects.filter(created_at__week_day=2)[:25]
In [75]: for r in list_reviews:
    ...:     print(r)
    ...: 
'Eight without.' от: Donald Phillips, оценка: 1, коментарий: Nothing blood way modern by make medical positive never at work pull food.
'Star owner.' от: David Hicks, оценка: 1, коментарий: President sign administration speak especially out tough girl since until contain.
'Work also professional.' от: Laura Sims, оценка: 1, коментарий: Interview ahead point wish cup attorney heart budget lot.
'Visit start lead.' от: Catherine Houston, оценка: 1, коментарий: Old factor purpose report century pass institution after wonder may course.
'Year agree.' от: Anna Flores, оценка: 4, коментарий: Cost yard add figure investment ten surface impact citizen however.
'Involve tell for.' от: Elizabeth Harrington, оценка: 4, коментарий: Notice pattern administration practice national sister remember government institution answer president.
'Along next history.' от: Jonathan Hayes, оценка: 4, коментарий: Stay great smile raise body front challenge relate base sure grow.
'During friend floor.' от: Taylor Jones, оценка: 5, коментарий: Chance along child large dinner air girl.
'Number into.' от: William Kline, оценка: 3, коментарий: Charge and situation ok step success suddenly sport song despite soldier seem agency age.
'North it.' от: Melissa Smith, оценка: 1, коментарий: Cultural pay stage time beautiful young through today full receive class view action.
'Last believe help.' от: Jacob Decker, оценка: 5, коментарий: Top down account finish memory front sometimes technology.
'Beyond either reach.' от: Anthony Wright, оценка: 3, коментарий: Above spend get defense skin travel keep finish yard young.
'At office.' от: Jaclyn Smith, оценка: 2, коментарий: Bit style real rather break particular along.
'Bag rich marriage.' от: Angela Fox, оценка: 5, коментарий: Part education prevent worker name find support only what agent.
'Certain main dark.' от: Monica Hardin, оценка: 1, коментарий: Reflect ability street hour process begin question yes let food commercial perhaps piece.
'Fish want main.' от: Craig Gillespie, оценка: 5, коментарий: Moment chair executive design such important raise difficult.
'Individual important laugh.' от: Brandi Robinson, оценка: 1, коментарий: Require leave manager yeah matter in room college account admit second teach list.
'Listen door law.' от: James Hernandez, оценка: 5, коментарий: Individual provide dark worker between control might actually apply board.
'Yourself.' от: William Ramos, оценка: 3, коментарий: Grow yeah again within forget color bar.
'Sense scene power.' от: Alexander Sanchez, оценка: 5, коментарий: Present check important them important make above.
'Record great its.' от: Jeffrey Burch, оценка: 3, коментарий: On team writer hard edge value political future.
'Attack pressure car.' от: Andrew Ramirez, оценка: 4, коментарий: Need hand third miss range rate free claim stay measure them her either.
'Turn thought.' от: Billy Valentine, оценка: 4, коментарий: Fight during turn matter career response offer sea meet move vote.
'Republican special.' от: Aimee Edwards, оценка: 4, коментарий: Model sport pretty how build forward eat three.
'Most member.' от: Jessica Vaughn, оценка: 2, коментарий: Institution camera foreign do they break fund. 
    
24. Найди книги, опубликованные во втором квартале года. 
In [76]: list_books = Book.objects.filter(published_date__month__in=[4, 5, 6])[:25]
In [77]: for b in list_books:
    ...:     print(b)
    ...: 
'Professional keep.', от: Victor Kelly - memorymadisonmoore@example.com, опубликовано: 2020-06-28 22:49:55.351064+00:00, цена:1295.24,скидка: 395.76, доп данные:{'genre': 'player', 'pages': 132}
'Meeting environment.', от: Donald Zhang - servemarylewis@example.net, опубликовано: 2023-06-16 10:05:45.086483+00:00, цена:1168.09,скидка: 357.66, доп данные:{'genre': 'from', 'pages': 131}
'Explain store general.', от: Corey Blackwell - agobecky22@example.org, опубликовано: 2021-05-18 14:19:34.280770+00:00, цена:4397.39,скидка: 184.80, доп данные:{'genre': 'under', 'pages': 195}
'To seem live.', от: Kelly Wong - professorduncanzachary@example.net, опубликовано: 2025-06-15 18:10:38.601416+00:00, цена:3554.58,скидка: 289.80, доп данные:{'genre': 'opportunity', 'pages': 451}
'Personal.', от: Kelly Hardy - leastgarciaryan@example.net, опубликовано: 2020-06-14 21:58:05.944401+00:00, цена:4295.98,скидка: 161.00, доп данные:{'genre': 'store', 'pages': 340}
'Film local technology somebody.', от: Timothy Allen - anythingkelleyjessica@example.com, опубликовано: 2024-04-16 21:34:13.559933+00:00, цена:532.95,скидка: 437.56, доп данные:{'genre': 'serve', 'pages': 346}
'Your value.', от: Margaret Pena - purposebridgetdavis@example.org, опубликовано: 2025-04-06 06:03:55.901639+00:00, цена:4257.08,скидка: 2.16, доп данные:{'genre': 'reality', 'pages': 204}
'Protect drug.', от: Angela Shaw - weekohumphrey@example.com, опубликовано: 2023-04-10 05:58:22.841906+00:00, цена:596.32,скидка: 282.24, доп данные:{'genre': 'benefit', 'pages': 175}
'Total usually.', от: Jorge Mcdowell - westernmendozaandrew@example.org, опубликовано: 2022-05-05 01:59:54.107788+00:00, цена:1397.07,скидка: 422.65, доп данные:{'genre': 'site', 'pages': 180}
'Cut hotel.', от: Jonathan Elliott - Mrdanielwright@example.org, опубликовано: 2021-06-11 04:59:18.930929+00:00, цена:1464.49,скидка: 243.78, доп данные:{'genre': 'yourself', 'pages': 366}
'Account cover pick.', от: Sarah Hall - againstdonaldali@example.org, опубликовано: 2025-04-19 15:50:15.471072+00:00, цена:3791.59,скидка: 107.01, доп данные:{'genre': 'follow', 'pages': 345}
'Throw.', от: Christina Gutierrez - bagshane45@example.com, опубликовано: 2021-04-19 08:24:02.343942+00:00, цена:1466.72,скидка: 13.91, доп данные:{'genre': 'citizen', 'pages': 131}
'Drug research.', от: Andrew Johnson - positivedebbie25@example.com, опубликовано: 2022-05-16 15:03:34.632036+00:00, цена:2150.72,скидка: 442.39, доп данные:{'genre': 'stage', 'pages': 260}
'Popular represent run.', от: Melissa Williams - seriesheatherhall@example.org, опубликовано: 2020-05-29 06:14:42.868814+00:00, цена:4133.13,скидка: 207.05, доп данные:{'genre': 'marriage', 'pages': 190}
'Support add.', от: Matthew Morrison - situationfitzgeraldtammy@example.com, опубликовано: 2022-04-12 11:14:14.695894+00:00, цена:877.40,скидка: 203.48, доп данные:{'genre': 'style', 'pages': 263}
'Peace ground break.', от: Charles Mann - himbrookstammy@example.com, опубликовано: 2025-04-06 01:51:30.171762+00:00, цена:613.37,скидка: 409.99, доп данные:{'genre': 'those', 'pages': 383}
'Worry conference.', от: Daniel Stone - magazinebenjaminsaunders@example.com, опубликовано: 2023-04-20 15:10:52.078236+00:00, цена:1284.96,скидка: 286.58, доп данные:{'genre': 'drive', 'pages': 329}
'Point soldier.', от: Diane Mata - paperjhill@example.com, опубликовано: 2025-04-04 16:14:51.406967+00:00, цена:1037.54,скидка: 18.98, доп данные:{'genre': 'future', 'pages': 284}
'However those involve.', от: Darren Molina - forwardiforbes@example.net, опубликовано: 2020-05-09 18:33:49.421412+00:00, цена:903.56,скидка: 157.76, доп данные:{'genre': 'thus', 'pages': 266}
'Go house.', от: Ralph Thomas - hospitalmendezjames@example.net, опубликовано: 2024-04-24 03:54:07.436451+00:00, цена:3360.12,скидка: 43.53, доп данные:{'genre': 'case', 'pages': 402}
'Power personal evidence.', от: Amber Crawford - dogdaniel39@example.com, опубликовано: 2022-06-19 16:45:21.558637+00:00, цена:3169.35,скидка: 253.44, доп данные:{'genre': 'population', 'pages': 248}
'Middle.', от: Jason Parks - secondrobinsonvictor@example.com, опубликовано: 2024-04-02 07:44:04.908302+00:00, цена:2075.12,скидка: 317.24, доп данные:{'genre': 'onto', 'pages': 361}
'Thus rise.', от: Peter Brewer - rangehernandezdavid@example.net, опубликовано: 2023-05-20 04:24:35.402838+00:00, цена:3444.06,скидка: 104.08, доп данные:{'genre': 'really', 'pages': 380}
'Century explain rich.', от: Lindsey Conrad - acceptegarcia@example.org, опубликовано: 2023-05-07 09:52:14.338361+00:00, цена:3657.27,скидка: 147.50, доп данные:{'genre': 'analysis', 'pages': 242}
'Item religious assume.', от: Taylor Solomon - certainlyjimenezjames@example.net, опубликовано: 2025-04-11 16:15:09.489693+00:00, цена:788.90,скидка: 143.40, доп данные:{'genre': 'modern', 'pages': 212}

25. Найди отзывы, сделанные в определённую дату.  
In [85]: Review.objects.filter(created_at__date='2025-07-07')[:1]
Out[85]: <QuerySet [<Review: 'Eight without.' от: Donald Phillips, оценка: 1, коментарий: Nothing blood way modern by make medical positive never at work pull food.>]> 
    
26. Найди отзывы, сделанные ровно в 15:30.  
In [86]: list_reviews = Review.objects.filter(created_at__time='15:30:00')[:25]
In [88]: list_reviews
Out[88]: <QuerySet []>
    
27. Найди отзывы, сделанные в 15 часов.  
In [89]: list_reviews = Review.objects.filter(created_at__time='15:00:00')[:25]
In [90]: list_reviews
Out[90]: <QuerySet []>
      
28. Найди отзывы, сделанные в 30 минут любого часа.
In [93]: list_reviews = Review.objects.filter(created_at__minute=30)
In [94]: list_reviews
Out[94]: <QuerySet []>
    
29. Найди отзывы, созданные в момент, когда секунды были равны 0.
In [95]: list_reviews = Review.objects.filter(created_at__second=0)
In [96]: list_reviews
Out[96]: <QuerySet []>

### Связанные поля
30. Найди книги, написанные автором с почтой «author@example.com».  
In [97]: Book.objects.filter(author__email='author@example.com')
Out[97]: <QuerySet []> 
    
31. Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра).   
In [101]: for b in list_books:
     ...:     print(b)
     ...: 
'Author try charge.', от: John Smith - statementjackhardy@example.org, опубликовано: 2024-01-17 17:29:27.206612+00:00, цена:4769.70,скидка: 370.92, доп данные:{'genre': 'it', 'pages': 293}
'Big per.', от: John Smith - statementjackhardy@example.org, опубликовано: 2025-01-28 19:00:02.633456+00:00, цена:4060.18,скидка: 49.76, доп данные:{'genre': 'toward', 'pages': 129}
'Four exactly.', от: John Smith - statementjackhardy@example.org, опубликовано: 2020-12-19 21:23:01.416945+00:00, цена:2795.30,скидка: 131.23, доп данные:{'genre': 'stop', 'pages': 186}
'Street single early.', от: John Smith - statementjackhardy@example.org, опубликовано: 2020-11-19 10:13:37.486482+00:00, цена:4390.40,скидка: 348.68, доп данные:{'genre': 'stuff', 'pages': 155}
'Control give.', от: John Smith - statementjackhardy@example.org, опубликовано: 2021-05-14 14:36:06.510797+00:00, цена:3064.48,скидка: 445.33, доп данные:{'genre': 'staff', 'pages': 423}
'Knowledge mouth per.', от: John Smith - statementjackhardy@example.org, опубликовано: 2025-06-13 10:35:38.781062+00:00, цена:3623.21,скидка: 186.73, доп данные:{'genre': 'not', 'pages': 237}
'Collection yourself.', от: John Smith - statementjackhardy@example.org, опубликовано: 2022-12-01 15:29:39.567347+00:00, цена:3728.42,скидка: 51.77, доп данные:{'genre': 'meeting', 'pages': 135}
'Education pass create.', от: John Smith - statementjackhardy@example.org, опубликовано: 2023-07-17 07:21:32.409638+00:00, цена:3675.87,скидка: 314.55, доп данные:{'genre': 'way', 'pages': 314}
'Effect store.', от: John Smith - statementjackhardy@example.org, опубликовано: 2021-08-13 11:10:37.417356+00:00, цена:2416.18,скидка: 119.39, доп данные:{'genre': 'possible', 'pages': 383}
'Executive eat issue.', от: John Smith - statementjackhardy@example.org, опубликовано: 2020-05-12 01:46:06.428518+00:00, цена:2814.90,скидка: 286.67, доп данные:{'genre': 'line', 'pages': 405}
'Despite boy range.', от: Jeffrey Smith - wrongimiller@example.org, опубликовано: 2022-07-02 18:46:53.002784+00:00, цена:2836.80,скидка: 98.79, доп данные:{'genre': 'fact', 'pages': 369}
'Detail pattern magazine.', от: Jeffrey Smith - wrongimiller@example.org, опубликовано: 2021-02-11 22:23:50.868131+00:00, цена:3773.03,скидка: 436.72, доп данные:{'genre': 'organization', 'pages': 140}
'Arrive later.', от: Jeffrey Smith - wrongimiller@example.org, опубликовано: 2020-06-16 08:55:06.720373+00:00, цена:4237.19,скидка: 260.74, доп данные:{'genre': 'civil', 'pages': 172}
'Give account.', от: Jeffrey Smith - wrongimiller@example.org, опубликовано: 2023-02-20 07:12:19.084777+00:00, цена:4931.67,скидка: 125.48, доп данные:{'genre': 'guess', 'pages': 302}
'Happen sign stage discussion.', от: Jeffrey Smith - wrongimiller@example.org, опубликовано: 2024-06-17 12:59:26.445966+00:00, цена:4117.36,скидка: 247.05, доп данные:{'genre': 'shake', 'pages': 397}
'Truth late help.', от: Jeffrey Smith - wrongimiller@example.org, опубликовано: 2022-11-13 12:33:43.424413+00:00, цена:3129.04,скидка: 53.62, доп данные:{'genre': 'American', 'pages': 199}
'Drive else.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2024-11-07 07:56:12.166910+00:00, цена:2824.87,скидка: 147.97, доп данные:{'genre': 'develop', 'pages': 171}
'Example.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2021-02-14 08:33:37.944363+00:00, цена:4921.01,скидка: 365.37, доп данные:{'genre': 'require', 'pages': 435}
'Short.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2023-02-09 02:48:26.879170+00:00, цена:743.27,скидка: 326.58, доп данные:{'genre': 'style', 'pages': 387}
'Southern will.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2023-11-16 01:22:45.000597+00:00, цена:2432.77,скидка: 55.45, доп данные:{'genre': 'decision', 'pages': 216}
'Body tough pass.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2024-10-23 07:50:38.262651+00:00, цена:1717.91,скидка: 311.70, доп данные:{'genre': 'example', 'pages': 118}
'Religious first mission.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2022-12-07 01:01:34.505869+00:00, цена:1952.58,скидка: 201.91, доп данные:{'genre': 'traditional', 'pages': 194}
'Successful management safe.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2021-05-07 03:36:06.326579+00:00, цена:4114.34,скидка: 197.33, доп данные:{'genre': 'certainly', 'pages': 180}
'Item say.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2020-05-16 21:58:42.105629+00:00, цена:3687.10,скидка: 422.73, доп данные:{'genre': 'purpose', 'pages': 252}
'This Republican Democrat office.', от: Michael Smith - spacekristen00@example.net, опубликовано: 2022-11-16 19:24:28.391174+00:00, цена:2526.68,скидка: 164.61, доп данные:{'genre': 'authority', 'pages': 230}

32. Найди авторов, написавших более пяти книг.
In [130]: list_authors = Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=5)[:25]
In [131]: for author in list_authors:
     ...:     print(f"Автор: {author.first_name} {author.last_name}, Количество книг: {author.book_count}")
     ...: 
Автор: Richard Harrington, Количество книг: 10
Автор: Anne Richardson, Количество книг: 10
Автор: Douglas Li, Количество книг: 10
Автор: Bonnie Peterson, Количество книг: 8
Автор: Denise Lopez, Количество книг: 9
Автор: Samuel Gomez, Количество книг: 10
Автор: Philip Sanders, Количество книг: 10
Автор: Margaret Pena, Количество книг: 11
Автор: Holly Camacho, Количество книг: 9
Автор: Thomas Johnson, Количество книг: 7
Автор: Tina Lopez, Количество книг: 12
Автор: Jacob Dennis, Количество книг: 16
Автор: Jennifer Thompson, Количество книг: 8
Автор: David Morse, Количество книг: 7
Автор: Deborah Jones, Количество книг: 8
Автор: Mark Figueroa, Количество книг: 10
Автор: Steven Butler, Количество книг: 10
Автор: Timothy Russell, Количество книг: 9
Автор: James Lewis, Количество книг: 10
Автор: Jonathan Dixon, Количество книг: 10
Автор: Patricia Olson, Количество книг: 11
Автор: Robert Hall, Количество книг: 12
Автор: Derek Lopez, Количество книг: 10
Автор: John Smith, Количество книг: 10
Автор: Wayne Bryan, Количество книг: 6

### JSON-поля
33. Найди книги, у которых значение ключа «genre» равно «fiction».  
In [109]: Book.objects.filter(metadata__genre='fiction')
Out[109]: <QuerySet []>

34. Найди книги, где значение ключа «tags» содержит слово «bestseller» (игнорируя регистр). 
In [111]: Book.objects.filter(metadata__tags__icontains='bestseller')
Out[111]: <QuerySet []>

### Использование выражений F и Q
35. Найди книги, у которых цена равна скидке.  
In [112]: from django.db.models import Q
In [114]: from django.db.models import F
In [115]: Book.objects.filter(price=F('discount'))
Out[115]: <QuerySet []>
 
36. Найди книги, у которых цена больше скидки.  
In [118]: list_books = Book.objects.filter(price__gt=F('discount'))[:25]
In [119]: for b in list_books:
     ...:     print(b)
     ...: 
'Meeting letter mean.', от: Angela Escobar - certainlyhebertrobert@example.com, опубликовано: 2023-02-22 00:37:31.716172+00:00, цена:3344.98,скидка: 312.02, доп данные:{'genre': 'affect', 'pages': 148}
'Professional keep.', от: Victor Kelly - memorymadisonmoore@example.com, опубликовано: 2020-06-28 22:49:55.351064+00:00, цена:1295.24,скидка: 395.76, доп данные:{'genre': 'player', 'pages': 132}
'Meeting environment.', от: Donald Zhang - servemarylewis@example.net, опубликовано: 2023-06-16 10:05:45.086483+00:00, цена:1168.09,скидка: 357.66, доп данные:{'genre': 'from', 'pages': 131}
'New third story.', от: Eric Lee - winclarkdeanna@example.com, опубликовано: 2022-02-07 14:12:54.952720+00:00, цена:3276.58,скидка: 372.19, доп данные:{'genre': 'data', 'pages': 217}
'Exist executive.', от: William Richardson - endtwalker@example.net, опубликовано: 2020-03-22 04:05:09.242319+00:00, цена:4121.63,скидка: 251.97, доп данные:{'genre': 'soldier', 'pages': 262}
'Fear.', от: Brandon Mcknight - eventheresa60@example.org, опубликовано: 2023-11-25 02:28:17.794569+00:00, цена:2339.26,скидка: 88.25, доп данные:{'genre': 'writer', 'pages': 490}
'Year avoid.', от: Katrina Owen - maybejenglish@example.com, опубликовано: 2020-08-06 04:31:23.494417+00:00, цена:559.34,скидка: 140.81, доп данные:{'genre': 'team', 'pages': 463}
'Break nation.', от: Bonnie Hess - alonekimberlywilliams@example.com, опубликовано: 2024-07-30 21:59:22.048699+00:00, цена:855.60,скидка: 344.45, доп данные:{'genre': 'theory', 'pages': 212}
'Beyond respond consider.', от: Harold Wagner - nearlyahenry@example.org, опубликовано: 2024-02-24 20:06:18.649125+00:00, цена:4567.98,скидка: 334.74, доп данные:{'genre': 'unit', 'pages': 468}
'According might tend.', от: Amber Glover - roleycordova@example.net, опубликовано: 2022-12-10 22:52:37.428110+00:00, цена:778.90,скидка: 220.35, доп данные:{'genre': 'great', 'pages': 156}
'Explain store general.', от: Corey Blackwell - agobecky22@example.org, опубликовано: 2021-05-18 14:19:34.280770+00:00, цена:4397.39,скидка: 184.80, доп данные:{'genre': 'under', 'pages': 195}
'Painting decide.', от: Erin Robinson - awayafisher@example.com, опубликовано: 2021-01-13 05:48:47.603779+00:00, цена:2834.37,скидка: 227.06, доп данные:{'genre': 'though', 'pages': 148}
'To seem live.', от: Kelly Wong - professorduncanzachary@example.net, опубликовано: 2025-06-15 18:10:38.601416+00:00, цена:3554.58,скидка: 289.80, доп данные:{'genre': 'opportunity', 'pages': 451}
'Fact very.', от: Billy Valentine - arrivelongvanessa@example.com, опубликовано: 2020-09-01 20:10:07.733161+00:00, цена:1900.60,скидка: 56.77, доп данные:{'genre': 'middle', 'pages': 460}
'Low.', от: Eric Green - dealggarcia@example.org, опубликовано: 2020-09-08 19:34:08.540429+00:00, цена:2600.32,скидка: 437.09, доп данные:{'genre': 'best', 'pages': 344}
'Sing.', от: Stephanie Castro - wondermelissa45@example.net, опубликовано: 2021-01-27 23:32:18.693934+00:00, цена:3792.01,скидка: 20.85, доп данные:{'genre': 'defense', 'pages': 137}
'Personal.', от: Kelly Hardy - leastgarciaryan@example.net, опубликовано: 2020-06-14 21:58:05.944401+00:00, цена:4295.98,скидка: 161.00, доп данные:{'genre': 'store', 'pages': 340}
'Instead thank.', от: Nicole Jimenez - firstchristopher00@example.com, опубликовано: 2023-08-26 03:21:51.787934+00:00, цена:3845.65,скидка: 341.32, доп данные:{'genre': 'popular', 'pages': 174}
'Industry large.', от: John Romero - voicerogersmark@example.org, опубликовано: 2020-03-02 08:03:39.600936+00:00, цена:1526.15,скидка: 67.95, доп данные:{'genre': 'agreement', 'pages': 232}
'Film local technology somebody.', от: Timothy Allen - anythingkelleyjessica@example.com, опубликовано: 2024-04-16 21:34:13.559933+00:00, цена:532.95,скидка: 437.56, доп данные:{'genre': 'serve', 'pages': 346}
'Adult once lead.', от: Eric Stevenson - commercialcheryl05@example.net, опубликовано: 2022-01-29 12:48:04.840868+00:00, цена:4797.42,скидка: 135.98, доп данные:{'genre': 'sport', 'pages': 108}
'Political fire.', от: Carlos Bird - preparesgarrison@example.net, опубликовано: 2020-10-23 10:09:45.968190+00:00, цена:3244.97,скидка: 289.99, доп данные:{'genre': 'exactly', 'pages': 493}
'Travel college condition.', от: Brittany Harding - explainlisa82@example.org, опубликовано: 2022-11-28 08:49:14.605953+00:00, цена:3732.66,скидка: 359.33, доп данные:{'genre': 'range', 'pages': 446}
'Step accept senior.', от: Angela Ayers - thoughtakramer@example.org, опубликовано: 2021-09-22 08:32:39.470432+00:00, цена:3287.96,скидка: 175.65, доп данные:{'genre': 'prove', 'pages': 406}
'We current popular.', от: Michele Williamson - strongjosephjones@example.org, опубликовано: 2024-08-25 13:31:12.192678+00:00, цена:3798.76,скидка: 407.86, доп данные:{'genre': 'second', 'pages': 267}
 
37. Найди авторов с именем «Alice» или с фамилией, не равной «Brown».
In [121]: list_authors = Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))[:25]
In [122]: for a in list_authors:
     ...:     print(a)
     ...: 
Richard Harrington - sharetuckeromar@example.net
Anne Richardson - loseobrienmichael@example.net
Douglas Li - smilexjuarez@example.org
Bonnie Peterson - yardstephaniemorris@example.com
Denise Lopez - politicalstephanie92@example.net
Samuel Gomez - rateocarr@example.net
Philip Sanders - comparethompsoncathy@example.org
Margaret Pena - purposebridgetdavis@example.org
Holly Camacho - airjohnstephens@example.org
Thomas Johnson - believeevan75@example.net
Tina Lopez - usuallychristina91@example.com
Jacob Dennis - everybodyhbryant@example.net
Jennifer Thompson - preparewilliamsmith@example.org
David Morse - benefitkenneth47@example.com
Alisha Blanchard - sameashley15@example.org
Deborah Jones - northqgarrett@example.org
Dustin Moore - maybeswhite@example.com
Mark Figueroa - newssharonbyrd@example.com
Steven Butler - factorlgreene@example.org
Timothy Russell - ballbward@example.org
James Lewis - choosefrankkenneth@example.net
Jonathan Dixon - serioustamarafisher@example.net
Patricia Olson - knowamartin@example.net
Robert Hall - nightzgardner@example.com
Derek Lopez - forcejames90@example.net

### Задания на аннотации
38. Подсчитай количество книг каждого автора.  
In [129]: list_book_authors = Author.objects.annotate(book_count=Count('books'))[:25]
     ...: 
     ...: for author in list_book_authors:
     ...:     print(f"Автор: {author.first_name} {author.last_name}, Количество книг: {author.book_count}")
     ...: 
Автор: Richard Harrington, Количество книг: 10
Автор: Anne Richardson, Количество книг: 10
Автор: Douglas Li, Количество книг: 10
Автор: Bonnie Peterson, Количество книг: 8
Автор: Denise Lopez, Количество книг: 9
Автор: Samuel Gomez, Количество книг: 10
Автор: Philip Sanders, Количество книг: 10
Автор: Margaret Pena, Количество книг: 11
Автор: Holly Camacho, Количество книг: 9
Автор: Thomas Johnson, Количество книг: 7
Автор: Tina Lopez, Количество книг: 12
Автор: Jacob Dennis, Количество книг: 16
Автор: Jennifer Thompson, Количество книг: 8
Автор: David Morse, Количество книг: 7
Автор: Alisha Blanchard, Количество книг: 2
Автор: Deborah Jones, Количество книг: 8
Автор: Dustin Moore, Количество книг: 5
Автор: Mark Figueroa, Количество книг: 10
Автор: Steven Butler, Количество книг: 10
Автор: Timothy Russell, Количество книг: 9
Автор: James Lewis, Количество книг: 10
Автор: Jonathan Dixon, Количество книг: 10
Автор: Patricia Olson, Количество книг: 11
Автор: Robert Hall, Количество книг: 12
Автор: Derek Lopez, Количество книг: 10

39. Подсчитай средний рейтинг каждой книги.  
In [135]: list_books = Book.objects.annotate(average_rating=Avg('reviews__rating'))[:25]
In [136]: for book in list_books:
     ...:     print(f"Название: {book.title}, автор: {book.author.first_name} {book.author.last_name}, средний рейтинг - {book.average_rating}")
     ...: 
Название: Meeting letter mean., автор: Angela Escobar, средний рейтинг - 3.25
Название: Professional keep., автор: Victor Kelly, средний рейтинг - 3.5714285714285716
Название: Meeting environment., автор: Donald Zhang, средний рейтинг - 3.0
Название: New third story., автор: Eric Lee, средний рейтинг - 3.0
Название: Exist executive., автор: William Richardson, средний рейтинг - 2.3333333333333335
Название: Fear., автор: Brandon Mcknight, средний рейтинг - 2.6
Название: Year avoid., автор: Katrina Owen, средний рейтинг - 3.3333333333333335
Название: Break nation., автор: Bonnie Hess, средний рейтинг - 2.6153846153846154
Название: Beyond respond consider., автор: Harold Wagner, средний рейтинг - 2.857142857142857
Название: According might tend., автор: Amber Glover, средний рейтинг - 3.5
Название: Explain store general., автор: Corey Blackwell, средний рейтинг - 3.2727272727272725
Название: Painting decide., автор: Erin Robinson, средний рейтинг - 3.2727272727272725
Название: To seem live., автор: Kelly Wong, средний рейтинг - 2.875
Название: Fact very., автор: Billy Valentine, средний рейтинг - 2.75
Название: Low., автор: Eric Green, средний рейтинг - 2.875
Название: Sing., автор: Stephanie Castro, средний рейтинг - 2.6363636363636362
Название: Personal., автор: Kelly Hardy, средний рейтинг - 3.0
Название: Instead thank., автор: Nicole Jimenez, средний рейтинг - 3.555555555555556
Название: Industry large., автор: John Romero, средний рейтинг - 2.75
Название: Film local technology somebody., автор: Timothy Allen, средний рейтинг - 2.0
Название: Adult once lead., автор: Eric Stevenson, средний рейтинг - 3.3636363636363638
Название: Political fire., автор: Carlos Bird, средний рейтинг - 3.555555555555556
Название: Travel college condition., автор: Brittany Harding, средний рейтинг - 2.642857142857143
Название: Step accept senior., автор: Angela Ayers, средний рейтинг - 3.7142857142857144
Название: We current popular., автор: Michele Williamson, средний рейтинг - 3.2857142857142856

40. Посчитай окончательную цену книги (цена минус скидка). 
In [138]: list_books = Book.objects.annotate(final_price=F('price') - F('discount'))[:25]
In [140]: for book in list_books:
     ...:     print(f"Название: {book.title}, Окончательная цена: {book.final_price}")
     ...: 
Название: Meeting letter mean., Окончательная цена: 3032.96
Название: Professional keep., Окончательная цена: 899.48
Название: Meeting environment., Окончательная цена: 810.43
Название: New third story., Окончательная цена: 2904.39
Название: Exist executive., Окончательная цена: 3869.66
Название: Fear., Окончательная цена: 2251.01
Название: Year avoid., Окончательная цена: 418.53
Название: Break nation., Окончательная цена: 511.15
Название: Beyond respond consider., Окончательная цена: 4233.24
Название: According might tend., Окончательная цена: 558.55
Название: Explain store general., Окончательная цена: 4212.59
Название: Painting decide., Окончательная цена: 2607.31
Название: To seem live., Окончательная цена: 3264.78
Название: Fact very., Окончательная цена: 1843.83
Название: Low., Окончательная цена: 2163.23
Название: Sing., Окончательная цена: 3771.16
Название: Personal., Окончательная цена: 4134.98
Название: Instead thank., Окончательная цена: 3504.33
Название: Industry large., Окончательная цена: 1458.20
Название: Film local technology somebody., Окончательная цена: 95.39
Название: Adult once lead., Окончательная цена: 4661.44
Название: Political fire., Окончательная цена: 2954.98
Название: Travel college condition., Окончательная цена: 3373.33
Название: Step accept senior., Окончательная цена: 3112.31
Название: We current popular., Окончательная цена: 3390.90

### Использование select_related и prefetch_related
41. Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос.
In [1]: list_books_authors = Book.objects.select_related('author')[:25]
   ...: 
   ...: for ba in list_books_authors:
   ...:     print(f"Название: {ba.title}, автор: {ba.author.first_name} {ba.author.last_name}")
   ...: 
SELECT "books_book"."id",
       "books_book"."title",
       "books_book"."author_id",
       "books_book"."published_date",
       "books_book"."price",
       "books_book"."discount",
       "books_book"."metadata",
       "books_author"."id",
       "books_author"."first_name",
       "books_author"."last_name",
       "books_author"."email",
       "books_author"."is_active"
  FROM "books_book"
 INNER JOIN "books_author"
    ON ("books_book"."author_id" = "books_author"."id")
 LIMIT 25
Execution time: 0.004925s [Database: default]
Название: Meeting letter mean., автор: Angela Escobar
Название: Professional keep., автор: Victor Kelly
Название: Meeting environment., автор: Donald Zhang
Название: New third story., автор: Eric Lee
Название: Exist executive., автор: William Richardson
Название: Fear., автор: Brandon Mcknight
Название: Year avoid., автор: Katrina Owen
Название: Break nation., автор: Bonnie Hess
Название: Beyond respond consider., автор: Harold Wagner
Название: According might tend., автор: Amber Glover
Название: Explain store general., автор: Corey Blackwell
Название: Painting decide., автор: Erin Robinson
Название: To seem live., автор: Kelly Wong
Название: Fact very., автор: Billy Valentine
Название: Low., автор: Eric Green
Название: Sing., автор: Stephanie Castro
Название: Personal., автор: Kelly Hardy
Название: Instead thank., автор: Nicole Jimenez
Название: Industry large., автор: John Romero
Название: Film local technology somebody., автор: Timothy Allen
Название: Adult once lead., автор: Eric Stevenson
Название: Political fire., автор: Carlos Bird
Название: Travel college condition., автор: Brittany Harding
Название: Step accept senior., автор: Angela Ayers
Название: We current popular., автор: Michele Williamson

42. Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса.
In [4]: list_authors_books = Author.objects.prefetch_related('books')[:25]
   ...: 
   ...: for author in list_authors_books:
   ...:     print(f"Автор: {author.first_name} {author.last_name},")
   ...:     for book in author.books.all():
   ...:         print(f"  Название: {book.title}")
   ...: 
SELECT "books_author"."id",
       "books_author"."first_name",
       "books_author"."last_name",
       "books_author"."email",
       "books_author"."is_active"
  FROM "books_author"
 LIMIT 25
Execution time: 0.000411s [Database: default]
SELECT "books_book"."id",
       "books_book"."title",
       "books_book"."author_id",
       "books_book"."published_date",
       "books_book"."price",
       "books_book"."discount",
       "books_book"."metadata"
  FROM "books_book"
 WHERE "books_book"."author_id" IN (2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)
Execution time: 0.001034s [Database: default]
Автор: Richard Harrington,
  Название: Yeah star same.
  Название: Ground child student.
  Название: Analysis model PM.
  Название: Physical probably that floor.
  Название: Enjoy off speech.
  Название: Successful when.
  Название: Everyone reflect option.
  Название: Reflect.
  Название: Media first present.
  Название: He say decide.
Автор: Anne Richardson,
  Название: Ball rich.
  Название: Example indicate.
  Название: Some.
  Название: With hit.
  Название: Pattern.
  Название: Congress whatever.
  Название: Development guy.
  Название: Step good.
  Название: Floor quality road first.
  Название: West get.
Автор: Douglas Li,
  Название: His stay.
  Название: Tend during turn pattern.
  Название: Fight win.
  Название: Boy visit.
  Название: Catch red side.
  Название: Clearly north herself small.
  Название: Subject claim another.
  Название: Chance.
  Название: Admit road should.
  Название: Very spend land.
Автор: Bonnie Peterson,
  Название: Best training subject.
  Название: None pattern.
  Название: Explain hand.
  Название: Bring amount.
  Название: Almost.
  Название: Paper case purpose.
  Название: Them financial.
  Название: Receive.
Автор: Denise Lopez,
  Название: New through break.
  Название: Front future relationship.
  Название: Employee help up develop.
  Название: Else large.
  Название: Easy one top give.
  Название: Either develop fish.
  Название: Walk soldier fear.
  Название: Offer interview time who.
  Название: Perhaps yeah just.
Автор: Samuel Gomez,
  Название: Yet look technology.
  Название: Write capital.
  Название: Detail on.
  Название: Safe culture.
  Название: Wall their high.
  Название: Skin answer.
  Название: Measure senior.
  Название: Window six house.
  Название: Kind summer yeah.
  Название: Prove morning.
Автор: Philip Sanders,
  Название: Mother drug.
  Название: Apply individual.
  Название: News.
  Название: Finish conference organization.
  Название: No fire race.
  Название: Especially many system.
  Название: Night measure left.
  Название: Of.
  Название: Stop sometimes.
  Название: Sense Congress glass.
Автор: Margaret Pena,
  Название: Your value.
  Название: Born building it.
  Название: Participant pass attention.
  Название: Next including most.
  Название: Professor strong nothing international.
  Название: Yourself support fast.
  Название: Expert cultural senior.
  Название: Majority piece.
  Название: Talk student foreign.
  Название: Spend agreement program teacher.
  Название: Five service.
Автор: Holly Camacho,
  Название: Father building show.
  Название: Among experience.
  Название: Nature cover decide some.
  Название: Run everybody production.
  Название: End example.
  Название: Author drug.
  Название: Through fund.
  Название: Western that hair.
  Название: Reality that likely.
Автор: Thomas Johnson,
  Название: Explain.
  Название: House early.
  Название: Commercial outside.
  Название: Join story charge.
  Название: Be catch property.
  Название: Kid painting.
  Название: Approach year Mr.
Автор: Tina Lopez,
  Название: Write third major.
  Название: Find whatever.
  Название: Civil play instead.
  Название: Level.
  Название: Position effort open.
  Название: Fund identify clear.
  Название: Same serve.
  Название: Sister themselves.
  Название: Today defense.
  Название: Many those.
  Название: Watch option.
  Название: Build.
Автор: Jacob Dennis,
  Название: Anyone economy.
  Название: Despite feeling.
  Название: This customer course.
  Название: Best such.
  Название: Note place management.
  Название: Different home participant.
  Название: Ten give brother.
  Название: Political choose.
  Название: Without send.
  Название: Someone we professional.
  Название: Team begin.
  Название: Spring president clearly.
  Название: Own face law.
  Название: Lead whom.
  Название: Story moment.
  Название: Such close chair.
Автор: Jennifer Thompson,
  Название: Want.
  Название: Large lead debate.
  Название: But me own.
  Название: Side exactly.
  Название: Prove century.
  Название: Again eye.
  Название: Practice almost poor.
  Название: Model government.
Автор: David Morse,
  Название: Likely that war.
  Название: Example.
  Название: Its land.
  Название: Citizen month dinner.
  Название: Human military well.
  Название: Together suggest.
  Название: Buy any everyone.
Автор: Alisha Blanchard,
  Название: Agreement price sister.
  Название: Form cause bar.
Автор: Deborah Jones,
  Название: Long whole seek.
  Название: Kind food.
  Название: What technology.
  Название: Find former.
  Название: Behavior measure.
  Название: Under identify away.
  Название: Life southern other.
  Название: Much beat.
Автор: Dustin Moore,
  Название: Rule.
  Название: West enough.
  Название: Already yet father.
  Название: Ground.
  Название: Week mention they.
Автор: Mark Figueroa,
  Название: Mr country.
  Название: Gun agree boy well.
  Название: Character truth take.
  Название: Stuff likely.
  Название: Crime new.
  Название: Hear stand president summer.
  Название: Popular second charge.
  Название: Television group away.
  Название: Military north.
  Название: Sort part involve.
Автор: Steven Butler,
  Название: Citizen modern.
  Название: Level stage general.
  Название: Method prepare.
  Название: Last politics table.
  Название: Whatever yeah one.
  Название: Culture be account.
  Название: Off radio against.
  Название: Different.
  Название: Successful on.
  Название: Citizen difficult focus better.
Автор: Timothy Russell,
  Название: Tv side camera.
  Название: Customer treat population.
  Название: End young you kitchen.
  Название: Tonight by time.
  Название: Owner bed real place.
  Название: Design couple.
  Название: Total.
  Название: Piece certainly.
  Название: Somebody dinner.
Автор: James Lewis,
  Название: Across model.
  Название: Carry.
  Название: Health.
  Название: Training parent.
  Название: Role benefit security.
  Название: Seat four.
  Название: Measure.
  Название: Build record.
  Название: Wind age public.
  Название: Improve country.
Автор: Jonathan Dixon,
  Название: Personal star.
  Название: Radio beat beautiful.
  Название: Wide professor onto.
  Название: Summer as professor.
  Название: Item whatever her.
  Название: Life wear.
  Название: I imagine.
  Название: Travel bit.
  Название: Floor heavy expert.
  Название: Seat fast group.
Автор: Patricia Olson,
  Название: Report ago.
  Название: Defense.
  Название: Main similar open.
  Название: Defense land cost campaign.
  Название: Similar care.
  Название: Hospital begin impact.
  Название: Stop.
  Название: Serious away why.
  Название: Southern bad order.
  Название: Talk catch name.
  Название: Daughter north.
Автор: Robert Hall,
  Название: Often staff.
  Название: Gas interest keep.
  Название: Major my.
  Название: Know poor main.
  Название: Civil population other.
  Название: Such recent central.
  Название: Inside western quality.
  Название: Attack fact.
  Название: Or social.
  Название: Purpose response computer two.
  Название: Care.
  Название: Capital fill become.
Автор: Derek Lopez,
  Название: Turn space adult.
  Название: State today.
  Название: Role yourself party.
  Название: Walk population.
  Название: End its TV.
  Название: Interview both need.
  Название: Figure improve phone enter.
  Название: Cell role.
  Название: Treatment ok.
  Название: Owner day new.