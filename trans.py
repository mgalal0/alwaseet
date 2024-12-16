from flask import Blueprint

trans = Blueprint("trans", __name__, template_folder="templates")

# Dictionary to store translations
# For Nav and Footer
# For All 
# BY GET ANY KEY
translations = {
    "en": {
        "Home": "Home",
        "About Us": "About Us",
        "Services": "Services",
        "Security Services": "Security Services",
        "Crowd Management": "Crowd Management",
        "Valet & Car Parking": "Valet & Car Parking",
        "Car Wash": "Car Wash Services",
        "Contact Us": "Contact Us",
        "Jobs": "Jobs",

        # About us Section 
        "About Us" : "About Us",
        "pabout"   : "Al Waseet is dedicated to enhancing the well-being of residents, visitors, and business owners in Saudi Arabia and Dubai. We not only provide top-notch security services but also offer a comprehensive range of additional services such as crowd management as well as valet & car parking services. These services are meticulously designed to contribute to a safe and comfortable environment in both regions.",
        "slogan" : "Al Waseet",


        # Our Primary Services
        "Our Primary Services":"Our Primary Services",
        "We always provide the best possible solutions" : "We always provide the best possible solutions" ,

        # Videos Section 
        "Our projects" : "Our projects",
        "Discover our highlights" : "Discover our highlights", 

        # Our Clinets 
        "Our Clients" : "Our Clients",

        # Team 
        "Al Waseet Team" : "Al Waseet Team",
        "pteam" : "These are the key roleplayers responsible for developing the effective and efficient solutions seen throughout the organisation.",

        "Mr. Ahmed Attar":"Mr. Ahmed Attar", 
        "Executive Manager":"Executive Manager", 

        "Mr. Raed Ali Elashry":"Mr. Raed Ali Elashry", 
        "General Manager":"General Manager", 

        "Dr. Mohamed Qutub":"Dr. Mohamed Qutub", 
        "Chief Executive Officer":"Chief Executive Officer",

        "Mr. Salem Saeed Al-Zahrani":"Mr. Salem Saeed Al-Zahrani", 
        "Security Manager":"Security Manager",

        "Mr. Stanley van der Merwe":"Mr. Stanley van der Merwe", 
        "Crowd Monagement Co-Ordinator":"Crowd Monagement Co-Ordinator",

        "Mr. Magdi Almass":"Mr. Magdi Almass", 
        "Operation Manager":"Operation Manager ",

        # footer section 
        "Designed By":"Ⓒ Designed by" ,
        "ALL RIGHTS RESERVED":"ALL RIGHTS RESERVED",
        

        # contact us page 
         "Contact us" : "Contact us" ,
         "Get in touch today" :  "Get in touch today",
         "location" : "Jeddah / Riyadh / Dammam / Mecca / Medina and Dubai ",
         "Name" : "Name" , 
         "Email" : "Email" ,
         "Phone" : "Phone" ,
         "Message" : "Message" ,
         "Send a message" : "Send a message" ,
         "Please type your message here..." : "Please type your message here..." ,
         "full name" : "Enter  your full name " ,

    },
    "ar": {
        "Home": "الرئيسية",
        "About Us": "من نحن" ,
        "Services": "الخدمات",
        "Security Services": "خدمات الأمن",
        "Crowd Management": "خدمات ادارة الحشود",
        "Valet & Car Parking": "خدمات صف و ركن السيارات",
        "Car Wash": " خدمات غسيل السيارات",
        "Contact Us" : "تواصل معنا" ,
        "Jobs": "الوظائف"  ,
        # About us Section 
        "About Us" : "من نحن",
        "pabout" : "تفتخر الوسيط بتعزيز رفاهية السكان والزائرين وأصحاب الأعمال في المملكة العربية السعودية ودبي.   نحن لا نقدم فقط خدمات أمن متميزة ولكن نقدم أيضًا مجموعة شاملة من الخدمات الإضافية مثل إدارة الحشود وخدمات ركن السيارات . تم تصميم هذه الخدمات بدقة للمساهمة في توفير بيئة آمنة ومريحة في كلا المنطقتين. ",
        "slogan" : "الوسيط",

        # Our Primary Services
        "Our Primary Services":"خدماتنا الرئيسية",
        "We always provide the best possible solutions" : "نحن دائمًا نقدم أفضل الحلول الممكنة" ,

        # Videos Section 
        "Our projects" : "مشاريعنا",
        "Discover our highlights" : "اكتشف أهم العناوين", 

        # Our Clinets 
        "Our Clients" : "عملاءنا",


        # Team 
        "Al Waseet Team" : "فريق الوسيط",
        "pteam" : "هؤلاء هم الأدوار الرئيسية المسؤولة عن تطوير الحلول الفعّالة والكفّاء التي ترى في جميع أنحاء المنظمة.",
        "Mr. Ahmed Attar":"أ.احمد عطار", 
        "Executive Manager":" المدير التنفيذي", 

        "Mr. Raed Ali Elashry":"أ.رائد علي العشري", 
        "General Manager":"  المدير العام  ", 

        "Dr. Mohamed Qutub":"د.محمد قطب", 
        "Chief Executive Officer":"الرئيس التنفيذي",

        "Mr. Salem Saeed Al-Zahrani":"أ.سالم سعيد الزهراني", 
        "Security Manager":" مدير الأمن",

        "Mr. Stanley van der Merwe":"أ.ستانلي فان دير ميرفي", 
        "Crowd Monagement Co-Ordinator":"منسق ادارة الحشود",

        "Mr. Magdi Almass":"أ.مجدي الماس", 
        "Operation Manager":"مدير العمليات  ",

         # footer section 
        "Designed By":"Ⓒ تم الإنشاء بواسطة" ,
        "ALL RIGHTS RESERVED":"جميع الحقوق محفوظة",

         # contact us page 
         "Contact us" : "اتصل بنا" ,
         "Get in touch today" :  "تواصل معنا اليوم",
         "location" : "جدة / الرياض / الدمام / مكة المكرمة /المدينة المنورة ودبي ",
         "Name" : "الإسم" , 
         "Email" : "البريد الإلكتروني" ,
         "Phone" : "رقم الهاتف" ,
         "Message" : "الرسالة" ,
         "Send a message" : "إرسال" ,
         "full name" : "الرجاء إدخال اسمك بالكامل" ,
         "your email":"الرجاء إدخال البريد الإلكتروني الخاص بك",
         "your phone":"الرجاء إدخال  vrl hgihjt الخاص ب" ,
         "Please type your message here..." : "الرجاء أدخل رسالتك هنا...",
    },
}


# services sliders translations 
# slider1_translations = {
#     'en': {
#         'slider': [
#             {'title': 'The Experience Begins', 'description': 'Defining Security Services'},
#               {'title': 'good', 'description': 'jjk kkkkll'},
#                {'title': 'good', 'description': 'jjk kkkkl'}
         
#         ],
        
#     },
#     'ar': {
#         'slider': [
#             {'title': 'تبدأ التجربة', 'description': 'تعريف خدمات الأمن'},
#              {'title': 'تبدأ ', 'description': 'تعريف خدمات '},
#              {'title': 'تبدأ ', 'description': 'تعريف  '},
        
#         ],
      
#     }
# }
# Componets 

# For Galary Section 
translations_galary = {
    "en": {
        "Security Services": "Security is not merely a service; it's a commitment to safeguarding the well-being of our clients, their assets, and the environments in which they operate. At Al waseet, the essence of Security Services transcends conventional protection - it embodies a profound dedication to vigilance, adaptability, and proactive risk mitigation.",
        "Valet & Car Parking Services": "Our Valet & Car Parking Services raise the bar in terms of convenience and efficiency. It's more than simply parking; it's a seamless experience in which attendees can trust our skilled crew with their vehicles.",
        "Crowd Management": "Alwaseet is a company that specializes in providing expert crowd management solutions in order to guarantee the safety and comfort of event attendees. The behavior of the audience is meticulously planned and coordinated by our skilled team, which lowers congestion and potential risks.",
        "Car Wash Services": "In a world that thrives on convenience and efficiency, Al Waseet brings innovation to car care with its Digital Car Wash Services. We understand that your vehicle is not just a mode of transportation but a reflection of your lifestyle.",
    },
    "ar": {
        "خدمات الأمن": "الأمن ليس مجرد خدمة؛ بل هو التزام بحماية رفاهية عملائنا، وأصولهم، والبيئات التي يعملون فيها. في الوسيط، يتجاوز جوهر خدمات الأمن الحماية التقليدية - بل إنه يتجلى في تفانٍ عميق في اليقظة والقدرة على التكيف، والحد من المخاطر بشكل استباقي.",
        "خدمات صف و ركن السيارات" : "تعمل خدمات صف السيارات ومواقف السيارات لدينا على رفع المستوى من حيث الراحة و الكفاءة. إنها أكثر من مجرد وقوف السيارات ؛ إنها تجربة سلسة يمكن للحاضرين الوثوق بطاقمنا الماهر في سياراتهم.",
        "ادارة الحشود" : "شركة الوسيط متخصصة في تقديم حلول إدارة الحشود  لضمان سلامة وراحة حضور الفعاليات. يتم تخطيط سلوك الجمهور بدقة وتنسيقه بواسطة فريقنا الماهر، مما يقلل من التزاحم والمخاطر المحتملة.",
        "خدمه غسيل السيارات":   "في عالم يزدهر بالراحة والفعالية، تقدم الوسيط خدمات غسيل السيارات الرقمية المبتكرة. نحن نفهم أن سيارتك ليست مجرد وسيلة نقل بل انعكاس لأسلوب حياتك",

    },
}


# For Galary Section Security 
translations_galary2 = {
    "en": {
        "Security Services": "Security is not merely a service; it's a commitment to safeguarding the well-being of our clients, their assets, and the environments in which they operate. At Al waseet, the essence of Security Services transcends conventional protection - it embodies a profound dedication to vigilance, adaptability, and proactive risk mitigation.",
        "Security Approach": "Our  security solutions are not one-size-fits-all; they are meticulously tailored to the unique needs of each client and situation. We are more than just a security presence; we are the guardians of peace and confidence, ensuring that those we serve can focus on their core objectives without distraction or concern.",
        "Assessments of Client Premises": "In the course of our evaluations of client sites, we thoroughly investigate risk on-site in collaboration with the client. The creation of complete site maps and an exhaustive list of all risks, and hazards are part of these analyses. The client is then informed of our findings so they can act right away to mitigate the situation.",
        "Risk Assessments": "We specialize in carrying out Site Risk Assessments to carefully pinpoint potential risks and safety concerns at the particular site or premises of our clients. Our customized risk assessments examine the particulars of the client's business, location, and circumstances in-depth, allowing us to create security solutions that are precisely targeted and address the most pressing dangers.",
    },
    "ar": {
        "خدمات الأمن": "الأمن ليس مجرد خدمة؛ بل هو التزام بحماية رفاهية عملائنا، وأصولهم، والبيئات التي يعملون فيها. في الوسيط، يتجاوز جوهر خدمات الأمن الحماية التقليدية - بل إنه يتجلى في تفانٍ عميق في اليقظة والقدرة على التكيف، والحد من المخاطر بشكل استباقي.",
        "النهج الأمني": "حلولنا الأمنية ليست موحدة للجميع؛ هي مصممة بدقة خصيصًا لتلبية الاحتياجات الفريدة لكل عميل وموقف. نحن أكثر من مجرد وجود أمني؛ نحن حراس السلام و الثقة، مما يضمن أن أولئك الذين نخدمهم يمكنهم التركيز على جوهر الأهداف دون تشتيت أو قلق.",
        "تقييمات أماكن العميل": "اثناء تقييمنا لمواقع عملائنا، نقوم بدراسة المخاطر على الأرض بالتعاون مع العميل. وتشمل هذه التحاليل إنشاء خرائط مواقع كاملة وقائمة شاملة بجميع المخاطر والمخاطر. يتم إبلاغ العميل بنتائجنا ليكون قادرًا على التصرف على الفور للتخفيف من الوضع.",
        "تقييم المخاطر": "نحن متخصصون في إجراء تقييمات المخاطر في الموقع لتحديد بعناية المخاطر المحتملة والمخاوف الأمنية في الموقع أو الممتلكات الخاصة بعملائنا.  تقييمات المخاطر المخصصة لدينا تفحص تفاصيل عمل العميل وموقعه وظروفه بشكل عميق، مما يسمح لنا بإنشاء حلول أمنية مستهدفة بدقة تعالج أكثر الأخطار.",

    },
}


# For Galary Crowd
translations_galary3 = {
    "en": {
        "Crowd Management": "Alwaseet is a company that specializes in providing expert crowd management solutions in order to guarantee the safety and comfort of event attendees. The behavior of the audience is meticulously planned and coordinated by our skilled team, which lowers congestion and potential risks.",
        "Approach": "Alwaseet approaches crowd control and assistance in a proactive manner. This enables us to provide the highest level of safety and security for all event guests.",
        "Expert Planning": "At Alwaseet, we take pride in our ability to create event designs that are meticulously planned down to the last detail. Our skilled personnel create strategies that turn your event vision into a seamless reality, equipped with years of experience and cutting-edge equipment.",
        "Tailored Designing": "At Alwaseet, we embrace the art of Tailored Designing, where every event is a canvas waiting for a unique masterpiece. Our creative minds, coupled with a keen understanding of your aspirations, bring forth designs that not only align with your vision but also breathe life into it.",
        "Measured Communication":"In the realm of event management, effective communication is the linchpin of success. Alwaseet understands that every word spoken and every message conveyed holds significance. Through Measured Communication, we ensure that every interaction, from pre-event announcements to on-site guidance, is delivered with clarity and purpose.",
        "Clear Co-ordination":"Alwaseet takes pride in the art of Clear Coordination,where every element seamlessly harmonizes to create an unforgettable performance. Our dedicated team ensures that behind-the-scenes efforts translate into a flawless event experience for your audience.",
        "Entry & Exit Strategies":"We recognize that the trip into and out of an event is just as important as the event itself at Alwaseet. We ensure that participants' movements are seamless, producing lasting impressions that set the foundation for outstanding experiences through thorough planning, cutting-edge technology, and a commitment to convenience.",
        "Staff Expertise":"Behind every exceptional event lies a team of experts who understand the intricacies of their craft. At Al Waseet, our Staff Expertise stands as the backbone of our success. Our team, meticulously trained and experienced, possesses an innate understanding of event dynamics."
    },
    "ar": {
        "خدمات إدارة الحشود": "شركة الوسيط متخصصة في تقديم حلول إدارة الحشود  لضمان سلامة وراحة حضور الفعاليات. يتم تخطيط سلوك الجمهور بدقة وتنسيقه بواسطة فريقنا الماهر، مما يقلل من التزاحم والمخاطر المحتملة.",
        "النهج الأمني": "تعمل شركة الوسيط على السيطرة والمساعدة في التحكم بالحشود بطريقة استباقية. وهذا يتيح لنا توفير أعلى مستوى من السلامة والأمان لجميع ضيوف الحدث. ",

        "  لتخطيط الاحترافي": "نحن في الوسيط، نفتخر بقدرتنا على تصميم الفعاليات بدقة تامة حتى التفاصيل الأخيرة. يقوم فريقنا المؤهل بوضع استراتيجيات تجعل رؤيتك للحدث تصبح واقعاً سلساً، بسبب سنوات الخبرة وأحدث التجهيزات.",
       
       
       "التواصل المدروس": "في مجال إدارة الفعاليات، التواصل الفعّال هو المفتاح الرئيسي للنجاح. الوسيط يدرك أن كل كلمة تنطق وكل رسالة توصل تحمل أهمية كبيرة.من خلال التواصل المدروس، نضمن أن كل تفاعل، بدءًا من الإعلانات قبل الحدث وصولاً إلى التوجيه في الموقع، يتم تقديمه بوضوح وغاية معينة." ,
       "تنسيق واضح": " الوسيط يفخر بفن التنسيق الواضح، حيث يتناغم كل عنصر بسلاسة لإنشاء أداء لا يُنسى. يضمن فريقنا المخلص أن الجهود خلف الكواليس تتحول إلى تجربة حدث خالية من العيوب لجمهورك." ,
       "استراتيجيات الدخول والخروج": " ندرك أن الرحلة إلى الحدث وخارجه مهمة بنفس القدر من أهمية الحدث نفسه في الوسيط. نحرص على توفير حركة سلسة للمشاركين، وإنتاج انطباعات دائمة تمهد الطريق لتجارب ممتازة من خلال التخطيط الدقيق، وتقنيات الحد الأدنى، والالتزام بالراحة." ,

       "خبرة الموظفين": "وراء كل حدث استثنائي يقف فريق من الخبراء الذين يفهمون تفاصيل حرفتهم. في الوسيط، تقف خبرة فريق العمل كعمود فقري لنجاحنا. فريقنا، الذي تم تدريبه وتجربته بعناية فائقة، يمتلك فهماً طبيعياً لآلية الحدث."

       


    },
}



translations_galary4 = {
    "en": {
        "Valet & Car Parking Services": "Our Valet & Car Parking Services raise the bar in terms of convenience and efficiency. It's more than simply parking; it's a seamless experience in which attendees can trust our skilled crew with their vehicles.",
        "Optimised Parking Strategy": "Our Optimized Parking Strategy at Alwaseet demonstrates our dedication to ease and efficiency. We methodically plan designated parking zones, strategically situating them to maximize available space and facilitate traffic flow.",
    },
    "ar": {
        "خدمات صف و ركن السيارات" : "تعمل خدمات صف السيارات ومواقف السيارات لدينا على رفع المستوى من حيث الراحة و الكفاءة. إنها أكثر من مجرد وقوف السيارات ؛ إنها تجربة سلسة يمكن للحاضرين الوثوق بطاقمنا الماهر في سياراتهم.",
        "استراتيجية وقوف السيارات المحسنة":" استراتيجية توفير مواقف محسنة / تعكس استراتيجية التوقف الخاصة بنا في الوسيط تفانينا لتسهيل العمليات وزيادة الكفاءة. نخطط بشكل منهجي لتصميم مناطق الوقوف المخصصة، نضعها بشكل استراتيجي لتعظيم المساحة المتاحة وتيسير تدفق حركة المرور."
    },
}


translations_galary5 = {
    "en": {
        "Car Wash Services": "In a world that thrives on convenience and efficiency, Al Waseet brings innovation to car care with its Digital Car Wash Services. We understand that your vehicle is not just a mode of transportation but a reflection of your lifestyle.",
        "Approach": "Our skilled professionals use cutting-edge techniques and eco-friendly products to ensure your vehicle shines inside and out. Whether it's a routine clean or a meticulous detailing, you can trust Al Waseet for a level of quality that goes beyond expectations.",
        "Convenient Experience":"In a world where convenience is king, Al Waseet takes car care to the next level with its cutting-edge Digital Car Wash services. Say goodbye to the hassles of traditional car washes and embrace the future of automotive pampering.",
        "On-Demand Cleaning at Your Fingertips":"Imagine having the power to schedule a car wash with a few taps on your smartphone, wherever you are. With Al Waseet's digital platform, you can do just that. Our user-friendly app puts you in control, allowing you to request a car wash at a time and place that suits you.",
        "No More Queues, No More Waiting":"Traditional car washes often mean long queues and wasted hours. But with Al Waseet, you can skip the lines. Our digital service ensures that your car gets the attention it deserves without you ever having to leave your home or office. Efficiency is at the core of our digital car wash experience.",
        "Environmentally Conscious Cleaning":"We care about the environment, and our digital car wash reflects that. Our eco-friendly methods and water-saving techniques ensure that your car gets the shine it deserves without harming the planet. It's a win-win for you and Mother Earth.",
        "Professional Care on Your Terms":"Our team of skilled technicians is just a tap away. They arrive at your location fully equipped to deliver professional car cleaning services. From exterior shine to interior detailing, our experts ensure your vehicle leaves looking its best.",
        "Secure and Reliable":"We prioritize the security of your vehicle. Our digital platform offers secure payment options, and our technicians are vetted for your peace of mind. You can trust us to treat your car with care and professionalism.",
        "On-Site Car Cleaning":"Our Comprehensive Cleaning service takes car care to a whole new level. We believe in leaving no stone unturned, ensuring your vehicle not only looks its best but also feels fresh and inviting. Join us on a journey through the art of professional car detailing, where every inch of your vehicle is given the attention it deserves.",
        "Interior and Exterior Brilliance":"Al Waseet's on-site car cleaning goes beyond surface-level cleanliness. Our skilled technicians meticulously clean both the interior and exterior of your vehicle. From vacuuming and upholstery care to exterior washing and waxing, we ensure every nook and cranny of your car is attended to. The result? A vehicle that not only looks pristine on the outside but feels fresh and inviting on the inside, leaving you with a truly comprehensive",
        "Professional Attention to Detail":"At Al Waseet, we understand that each vehicle is unique, and our approach reflects this. Our skilled technicians have the expertise to cater to various vehicle types, addressing specific cleaning needs. Whether it's removing stubborn stains from your upholstery or giving your car's exterior a glossy shine, our attention to detail ensures that your vehicle leaves the event venue looking its absolute best. It's a level of professional care that goes above and beyond your expectations.",
        
    },
    "ar": {
        "خدمه غسيل السيارات":   "في عالم يزدهر بالراحة والفعالية، تقدم الوسيط خدمات غسيل السيارات الرقمية المبتكرة. نحن نفهم أن سيارتك ليست مجرد وسيلة نقل بل انعكاس لأسلوب حياتك",
        "النهج الأمني": "يستخدم المتخصصون المهرة لدينا أحدث التقنيات و منتجات صديقة للبيئة لضمان تألق سيارتك بالداخل وخارج. سواء كان ذلك نظيفا روتينيا أو دقيقا التفاصيل ، يمكنك الوثوق بالوسيط لمستوى الجودة الذي يتجاوز التوقعات.",
        "سهولة التجربة" : "رعاية إلى المستوى التالي مع غسيل السيارات الرقمي المتطور  خدمات. قل وداعا لمتاعب السيارات التقليدية يغسل ويحتضن مستقبل تدليل السيارات." ,
        "التنظيف عند الطلب في متناول يدك":"تخيل أن لديك القدرة على جدولة غسيل السيارات ببضع نقرات هاتفك الذكي، أينما كنت. مع منصة الوسيط الرقمية ، يمكنك أن تفعل ذلك بالضبط. تطبيقنا سهل الاستخدام يتيح لك التحكم ، مما يسمح يمكنك طلب غسيل السيارات في الوقت والمكان الذي يناسبك.",
        "لا مزيد من الطوابير ، لا مزيد من الانتظار ":"غالبا ما تعني مغاسل السيارات التقليدية طوابير طويلة وساعات ضائعة. ولكن مع آل الوسيط ، يمكنك تخطي الخطوط. تضمن خدمتنا الرقمية حصول سيارتك على الاهتمام الذي تستحقه دون الحاجة إلى مغادرة منزلك أو مكتبك.الكفاءة هي جوهر تجربتنا الرقمية لغسيل السيارات.",
        "تنظيف صديق للبيئة":"  نحن  نهتم بالبيئة ، ويعكس غسيل السيارات الرقمي لدينا ذلك. تضمن أساليبنا الصديقة للبيئة وتقنيات توفير المياه أن تحصل السيارة على اللمعان الذي تستحقه دون الإضرار بالكوكب. إنه فوز للجانبين لك ولأمنا الأرض.",
        "رعاية احترافية وفقا لشروطك":"دينا فريق من الفنيين المهرة على بعد نقرة واحدة. يصلون إلى موقع مجهز بالكامل لتقديم خدمات تنظيف السيارات الاحترافية. من اللمعان الخارجي إلى التفاصيل الداخلية ، يضمن خبراؤنا سيارتك يترك يبحث في أفضل حالاته.",
        "آمن و موثوق":"نحن نعطي الأولوية لأمن سيارتك. عروض منصتنا الرقمية خيارات دفع آمنة ، ويتم فحص الفنيين لدينا من أجل سلامك من العقل. يمكنك الوثوق بنا للتعامل مع سيارتك بعناية واحترافية.",
        "تنظيف سياره في الموقع":"خدمة التنظيف الشاملة لدينا تأخذ العناية بالسيارات إلى مستوى جديد كليا. نحن نؤمن بعدم ترك أي جهد دون قلب ، ضمان أن سيارتك لا تبدو في أفضل حالاتها فحسب ، بل تشعر أيضا طازجة وجذابة. انضم إلينا في رحلة عبر فن تفاصيل احترافية للسيارة ، حيث يوجد كل شبر من سيارتك بالنظر إلى الاهتمام الذي تستحقه.",
        "التألق الداخلي والخارجي":"نظيف السيارة في الموقع في الوسيط يتجاوز مستوى السطح النظافه. يقوم الفنيون المهرة لدينا بتنظيف كل من الداخل بدقة والجزء الخارجي من سيارتك. من التنظيف بالمكنسة الكهربائية والعناية بالمفروشات إلى الغسيل الخارجي وإزالة الشعر بالشمع ، نحن نضمن الاهتمام بكل زاوية وركن في سيارتك. ال نتيجة؟ سيارة لا تبدو نقية من الخارج فحسب ، بل تشعر أيضا بالراحة جديدة وجذابة من الداخل ، مما يتيح لك تجربة شاملة حقا",
        "لاهتمام المهني بالتفاصيل":"في الوسيط ، ندرك أن كل مركبة فريدة من نوعها ، ونهجنا يعكس هذا. يتمتع الفنيون المهرة لدينا بالخبرة اللازمة لتلبية احتياجات مختلف أنواع المركبات ، وتلبية احتياجات التنظيف المحددة. سواء كان ذلك لإزالة البقع العنيدة من مواد التنجيد الخاصة بك أو إعطاءالمظهر الخارجي للسيارة لمعان لامع ، اهتمامنا بالتفاصيل يضمن أن سيارتك يترك مكان الحدث يبدو في أفضل حالاته. إنه مستوى احترافي الرعاية التي تتجاوز توقعاتك.",

    },
}