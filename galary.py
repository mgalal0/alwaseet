from flask import Blueprint, render_template, url_for
galary = Blueprint("galary", __name__, template_folder="templates")

# meta tags 
meta_tags = {
    'ar': {
        'description': ' تفتخر الوسيط بتعزيز رفاهية السكان والزائرين وأصحاب الأعمال في المملكة العربية السعودية ودبي. نحن لا نقدم فقط خدمات أمن متميزة ولكن نقدم أيضًا مجموعة شاملة من الخدمات الإضافية مثل إدارة الحشود وخدمات ركن السيارات . تم تصميم هذه الخدمات بدقة للمساهمة في توفير بيئة آمنة ومريحة في كلا المنطقتين.  ',
        'keywords': ' خدمات الأمن  ,  خدمات ادارة الحشود , خدمات صف و ركن السيارات , خدمات غسيل السيارات '
    },
    'en': {
        'description': 'Al Waseet is dedicated to enhancing the well-being of residents, visitors, and business owners in Saudi Arabia and Dubai. We not only provide top-notch security services but also offer a comprehensive range of additional services such as crowd management as well as valet & car parking services. These services are meticulously designed to contribute to a safe and comfortable environment in both regions.',
        'keywords': 'Security Services, Crowd Management Services,Valet & Car Parking Services,Car Wash Services'
    }
}

# pages titles 
page_titles = {
    '/home': {'ar': ' الصفحة الرئيسية', 'en': 'Home Page '},
    '/security': {'ar': '  خدمات الأمن ', 'en': 'Security Services'},
    '/crowd': {'ar': ' خدمات ادارة الحشود', 'en': 'Crowd Management Services'},
    '/valet': {'ar': ' خدمات صف و ركن السيارات', 'en': 'Valet & Car Parking Services '},
    '/car-wash': {'ar': ' خدمات غسيل السيارات  ', 'en': 'Car Wash Services'},
    '/contact-us': {'ar': 'تواصل معنا', 'en': 'Contact Us'} ,
     '/jobs': {'ar': ' الوظائف', 'en': 'Jobs'} ,
    
    # Add more URLs and titles as needed
}
# Define a list of image filenames on primary services
image_filenames = ['images/card 1 (3).png', 'images/card 1 (1).png', 'images/card 1 (2).png' , 'images/card 1.png']

#imgs for security page galarywith sum
image_filenames2 = ['images/card 1 (3).png', 'images/galarywithsum/serv2/2.png', 'images/galarywithsum/serv2/3.png' , 'images/galarywithsum/serv2/4.png']

image_filenames3 = ['images/galarywithsum/serv3/1.png', 'images/galarywithsum/serv3/2.png', 'images/galarywithsum/serv3/3.png' , 'images/galarywithsum/serv3/4.png','images/galarywithsum/serv3/5.png','images/galarywithsum/serv3/6.png' , 'images/galarywithsum/serv3/7.png','images/galarywithsum/serv3/8.png']

image_filenames4 = ['images/galarywithsum/serv4/1.png', 'images/galarywithsum/serv4/2.png']



image_filenames5 = ['images/galarywithsum/serv5/1.png','images/card 1 (1).png' , 'images/galarywithsum/serv5/3.png' , 'images/galarywithsum/serv5/4.png','images/galarywithsum/serv5/5.png','images/galarywithsum/serv5/6.png' , 'images/galarywithsum/serv5/7.png','images/galarywithsum/serv5/8.png','images/galarywithsum/serv5/9.png','images/galarywithsum/serv5/10.png','images/galarywithsum/serv5/11.png']




banner_info = {
    '/security': {'image': 'serv-banner1', 'text': {'en': 'Security Services', 'ar': 'خدمات الأمن'},'btn-text':{'en':'Contact Us' ,'ar':'تواصل معنا'}},
    '/crowd': {'image': 'serv-banner2', 'text': {'en': 'Crowd Managment Services', 'ar': ' خدمات ادارة الحشود'},'btn-text':{'en':'Contact Us' ,'ar':'تواصل معنا'}},
    '/valet': {'image': 'serv-banner3', 'text': {'en': 'Valet & Car Parking Services', 'ar': ' خدمات صف و ركن السيارات '},'btn-text':{'en':'Contact Us' ,'ar':'تواصل معنا'}},
    '/car-wash': {'image': 'serv-banner4', 'text': {'en': 'Car Washing Services', 'ar': '  خدمات غسيل السيارات'},'btn-text':{'en':'Contact Us' ,'ar':'تواصل معنا'}}
}

# services slider 
sliders_info = {
    '/security': [
        {
            'image': 'images/serv-slider1/1.png',
            'heading': {'en': 'The Experience Begins ', 'ar': ' بداية التجربة'},
            'desc': {'en': 'Defining Security Services', 'ar': ' تعريف خدمات الأمن '}
        },
        {
            'image': 'images/serv-slider1/2.png',
            'heading': {'en': 'Tailored Approach', 'ar': '  استراتيجية مخصصة'},
            'desc': {'en': 'Developing tailored security plans', 'ar': ' لتطوير خطط الأمان'}
        },
         {
            'image': 'images/serv-slider1/3.png',
            'heading': {'en': 'Training Personnel', 'ar': '  موظفين متدربين'},
            'desc': {'en': 'Training to handle conflicts and emergencies', 'ar': '  تدريب الموظفين على التعامل مع الأزمات والطوارئ'}
        },
          {
            'image': 'images/serv-slider1/4.png',
            'heading': {'en': 'Surveillance Technology', 'ar': '  تكنولوجيا المراقبة'},
            'desc': {'en': 'The kinds of security equipment we use, and where', 'ar': '   أنواع معدات الأمان التي نستخدمها، ومكان استخدامها'}
        },
          {
            'image': 'images/serv-slider1/5.png',
            'heading': {'en': 'Collaborations', 'ar': '  التعاون '},
            'desc': {'en': 'We work hand-in-hand with local authorities', 'ar': '  نعمل بتنسيق وثيق مع القطاعات المحلية'}
        }
        
    ],
    '/crowd': [
        {
            'image': 'images/serv-slider2/1.png',
            'heading': {'en': 'The Experience Begins', 'ar': '  بداية التجربة'},
            'desc': {'en': 'Defining Crowd Monagement', 'ar': ' تعريف خدمات إدارة الحشود'}
        } ,
           {
            'image': 'images/serv-slider2/2.png',
            'heading': {'en': 'Tailored Approach', 'ar': '  استراتيجية مخصصة'},
            'desc': {'en': 'Entry&exit strategies', 'ar': ' استراتيجيات الدخول والخروج.'}
        } , 
           {
            'image': 'images/serv-slider2/3.png',
            'heading': {'en': 'Staff Expertise', 'ar': ' خبرة الموظفين '},
            'desc': {'en': 'Key role players&positions', 'ar': '  الأدوار الرئيسية والمواقع الرئيسية.'}
        } ,
           {
            'image': 'images/serv-slider2/4.png',
            'heading': {'en': 'Real-time Monitoring', 'ar': '  رصد الوقت الحقيقي'},
            'desc': {'en': 'Technologies used for real-time crowd  monitoring', 'ar': ' التقنيات المستخدمة لرصد الحشود في الوقت الحقيقي.'}
        } ,
           {
            'image': 'images/serv-slider2/5.png',
            'heading': {'en': 'Safety Response', 'ar': '  مسؤولية السلامة'},
            'desc': {'en': 'Approach to conflict resolution', 'ar': ' الوصول الى تسوية الخلافات'}
        } ,
           {
            'image': 'images/serv-slider2/6.png',
            'heading': {'en': 'Conflict Resolution', 'ar': '  حل الخلافات'},
            'desc': {'en': 'AlWaseets approach to de-escalation', 'ar': ' الطريقة التي يتبعها الوسيط في تسوية الخلافات'}
        }
    ],
    '/valet': [
        {
            'image': 'images/serv-slider3/1.png',
            'heading': {'en': 'The Al Waseet Expereince', 'ar': '  تجربة الوسيط  '},
            'desc': {'en': 'Defining Valet & Car Parking Services', 'ar': '  تعريف خدمات صف السيارات وخدمات ركن السيارات'}
        } ,
          {
            'image': 'images/serv-slider3/2.png',
            'heading': {'en': 'Tailored Approach', 'ar': ' استراتيجية مخصصة '},
            'desc': {'en': 'Optimised Parking Strategy', 'ar': 'إدارة وتحسين ركن  السيارات. '}
        },
          {
            'image': 'images/serv-slider3/3.png',
            'heading': {'en': 'Staff Expertise', 'ar': 'مؤشرات الأداء الرئيسية للعمليات '},
            'desc': {'en': 'We adhere to strict evaluation standards when hiring', 'ar': ' تنفيذ طريقة جديدة لإنشاء مؤشرات الأداء الرئيسية العملية .'}
        },
          {
            'image': 'images/serv-slider3/4.png',
            'heading': {'en': "Operations KPI's", 'ar': ' خبرة الموظفين'},
            'desc': {'en': 'Implement a novel way for establishing practical operational KPIs', 'ar': ' نلتزم بمعايير صارمة للتقييم عند التوظيف.'}
        },
          {
            'image': 'images/serv-slider3/5.png',
            'heading': {'en': "Equipment & Set-up", 'ar': 'تجهيز وترتيب المعدات'},
            'desc': {'en': 'Custom mode luxury Site set up', 'ar': ' إعداد موقع فاخر بنمط مخصص.'}
        },
    ],
    '/car-wash': [
        {
            'image': 'images/serv-slider4/1.png',
            'heading': {'en': 'The Al Waseet Expereince', 'ar': 'تجربة الوسيط '},
            'desc': {'en': 'Defining Car Washing Services', 'ar': '  تعريف خدمات غسيل السيارات'}
        },
           
    
          {
            'image': 'images/serv-slider4/2.png',
            'heading': {'en': 'Tailored Approach', 'ar': 'استراتيجية مخصصة  '},
            'desc': {'en': 'Convenient Experience', 'ar': '  تجربةٌ مريحة'}
        },
          {
            'image': 'images/serv-slider4/4.png',
            'heading': {'en': 'Revolutionizing Car Care', 'ar': 'ثورة في العناية بالسيارات'},
            'desc': {'en': 'Convenience and Efficiency Redefined: Your Vehicle, Your Lifestyle', 'ar': '  إعادة تعريف الراحة والكفاءة: سيارتك، أسلوب حياتك'}
        },
          {
            'image': 'images/serv-slider4/3.png',
            'heading': {'en': 'On-Site Car Cleaning', 'ar': 'تنظيف السيارات في الموقع '},
            'desc': {'en': 'The modes and methods used to ensure the best possible car wash', 'ar': '  الطرق والأساليب المستخدمة لضمان غسيل السيارات بأفضل جودة ممكنة'}
        }
         
    ]
}

# logos 
logos = [
    'images/logos/logo-1.svg' , 
    'images/logos/logo-1.svg' ,
]
# BackGround Sorted for Primary Services  

backgrounds_file = ['images/background/1.png','images/background/2.png','images/background/3.png','images/background/4.png']

# Album Photos
album1_images = [
 'images/album-home-imgs/1.png',
 'images/album-home-imgs/2.png',
 'images/album-home-imgs/3.png',
 'images/album-home-imgs/4.png',
 'images/album-home-imgs/5.png',
 'images/album-home-imgs/6.png',
 'images/album-home-imgs/7.png',
'images/album-home-imgs/8.png',
 'images/album-home-imgs/4.png',
 'images/album-home-imgs/5.png',
  'images/album-home-imgs/1.png',
 'images/album-home-imgs/2.png',
 'images/album-home-imgs/3.png',
  'images/album-home-imgs/6.png',
 'images/album-home-imgs/7.png',
'images/album-home-imgs/8.png',
'images/album-home-imgs/4.png',
 'images/album-home-imgs/5.png',
]
album2_images = [
 'images/album-home-imgs/9.png',
 'images/album-home-imgs/10.png',
 'images/album-home-imgs/11.png',
 'images/album-home-imgs/12.png',
 'images/album-home-imgs/13.png',
 'images/album-home-imgs/14.png',
  'images/album-home-imgs/15.png',
 'images/album-home-imgs/16.png',
 'images/album-home-imgs/17.png',
  'images/album-home-imgs/9.png',
 'images/album-home-imgs/10.png',
  'images/album-home-imgs/15.png',
 'images/album-home-imgs/16.png',
 'images/album-home-imgs/17.png',
 'images/album-home-imgs/11.png',
 'images/album-home-imgs/12.png',
 'images/album-home-imgs/13.png',
 'images/album-home-imgs/14.png',
  'images/album-home-imgs/15.png',
 'images/album-home-imgs/16.png',
 
]

# imgs for album2 in  security services page  -----------------------------
sec_album_1 = [
  'images/album2/21.png',
  'images/album2/22.png',
  'images/album2/23.png',
  'images/album2/24.png',
  'images/album2/25.png',
  'images/album2/27.png',
  'images/album2/28.png',
  'images/album2/29.png',
  'images/album2/21.png',
  'images/album2/22.png',
  'images/album2/23.png',
  'images/album2/24.png',
  'images/album2/25.png',
  'images/album2/27.png',
  'images/album2/28.png',
  'images/album2/29.png',
  'images/album2/21.png',
  'images/album2/22.png',
  'images/album2/23.png',
]
sec_album_2 = [
   'images/album2/210.png',
   'images/album2/211.png',
   'images/album2/212.png',
   'images/album2/213.png',
   'images/album2/214.png',
   'images/album2/215.png',
   'images/album2/216.png',
   'images/album2/217.png',
    'images/album2/210.png',
   'images/album2/211.png',
   'images/album2/212.png',
   'images/album2/213.png',
   'images/album2/214.png',
   'images/album2/215.png',
   'images/album2/216.png',
   'images/album2/217.png',
   'images/album2/210.png',
   'images/album2/211.png',
]

# imgs for album4 in valet page --------------------------------------
valet_album_1 = [
  'images/album4/41.png' ,
  'images/album4/42.png' ,
  'images/album4/43.png' ,
  'images/album4/44.png' ,
  'images/album4/45.png' ,
  'images/album4/46.png' ,
  'images/album4/47.png' ,
  'images/album4/48.png' ,
  'images/album4/49.png' ,
  'images/album4/41.png' ,
  'images/album4/42.png' ,
  'images/album4/43.png' ,
  'images/album4/44.png' ,
  'images/album4/45.png' ,
  'images/album4/46.png' ,
  'images/album4/47.png' ,
  'images/album4/48.png' ,
  'images/album4/49.png' ,
  'images/album4/41.png' ,
  'images/album4/42.png' ,

]
valet_album_2 = [
   'images/album4/410.png' ,
   'images/album4/411.png' ,
   'images/album4/412.png' ,
   'images/album4/413.png' ,
   'images/album4/414.png' ,
   'images/album4/415.png' ,
   'images/album4/416.png' ,
   'images/album4/417.png' ,
   'images/album4/418.png' ,
   'images/album4/410.png' ,
   'images/album4/411.png' ,
   'images/album4/412.png' ,
   'images/album4/413.png' ,
   'images/album4/414.png' ,
   'images/album4/415.png' ,
   'images/album4/416.png' ,
   'images/album4/417.png' ,
   'images/album4/418.png' ,
   'images/album4/410.png' ,
   'images/album4/411.png' ,

]
# imgs for album4 in car-wash page --------------------------------------
car_wash_album_1 = [
  'images/album5/31.png' ,
  'images/album5/32.png' ,
  'images/album5/33.png' ,
  'images/album5/34.png' ,
  'images/album5/35.png' ,
  'images/album5/36.png' ,
  'images/album5/37.png' ,
  'images/album5/38.png' ,
  'images/album5/39.png' ,
  'images/album5/31.png' ,
  'images/album5/32.png' ,
  'images/album5/33.png' ,
  'images/album5/34.png' ,
  'images/album5/35.png' ,
  'images/album5/36.png' ,
  'images/album5/37.png' ,
  'images/album5/38.png' ,
  'images/album5/39.png' ,
  'images/album5/31.png' ,
  'images/album5/32.png' ,
]
car_wash_album_2 = [
  'images/album5/310.png' ,
  'images/album5/311.png' ,
  'images/album5/312.png' ,
  'images/album5/313.png' ,
  'images/album5/314.png' ,
  'images/album5/315.png' ,
  'images/album5/316.png' ,
  'images/album5/317.png' ,
  'images/album5/318.png' ,
  'images/album5/319.png' ,
  'images/album5/310.png' ,
  'images/album5/311.png' ,
  'images/album5/312.png' ,
  'images/album5/313.png' ,
  'images/album5/314.png' ,
  'images/album5/315.png' ,
  'images/album5/316.png' ,
  'images/album5/317.png' ,
  'images/album5/318.png' ,
  'images/album5/319.png' ,
]

# imgs for album4 in crowd  page --------------------------------------
crowd_album_1 = [
  'images/album3/31.png' ,
  'images/album3/32.png' ,
  'images/album3/33.png' ,
  'images/album3/34.png' ,
  'images/album3/35.png' ,
  'images/album3/36.png' ,
  'images/album3/37.png' ,
  'images/album3/38.png' ,
  'images/album3/39.png' ,
  'images/album3/31.png' ,
  'images/album3/32.png' ,
  'images/album3/33.png' ,
  'images/album3/34.png' ,
  'images/album3/35.png' ,
  'images/album3/36.png' ,
  'images/album3/37.png' ,
  'images/album3/38.png' ,
  'images/album3/39.png' ,
  'images/album3/31.png' ,
  'images/album3/32.png' ,
  'images/album3/31.png' ,
  'images/album3/32.png' ,
]
crowd_album_2 = [
  'images/album3/310.png' ,
  'images/album3/311.png' ,
  'images/album3/312.png' ,
  'images/album3/313.png' ,
  'images/album3/314.png' ,
  'images/album3/315.png' ,
  'images/album3/316.png' ,
  'images/album3/317.png' ,
  'images/album3/318.png' ,
  'images/album3/310.png' ,
  'images/album3/311.png' ,
  'images/album3/312.png' ,
  'images/album3/313.png' ,
  'images/album3/314.png' ,
  'images/album3/315.png' ,
  'images/album3/316.png' ,
  'images/album3/317.png' ,
  'images/album3/318.png' ,
  'images/album3/310.png' ,
  'images/album3/311.png' ,
]
serv_slider1 = [
  'images/serv-slider1/1.png' ,
  'images/serv-slider1/2.png' ,
  'images/serv-slider1/3.png' ,
  'images/serv-slider1/4.png' ,
  'images/serv-slider1/5.png' ,
]

serv_slider2 = [
  'images/serv-slider2/1.png' ,
  'images/serv-slider2/2.png' ,
  'images/serv-slider2/3.png' ,
  'images/serv-slider2/4.png' ,
  'images/serv-slider2/5.png' ,
  'images/serv-slider2/6.png' ,
]

serv_slider3 = [
  'images/serv-slider3/1.png' ,
  'images/serv-slider3/2.png' ,
  'images/serv-slider3/3.png' ,
  'images/serv-slider3/4.png' ,
  'images/serv-slider3/5.png' ,
]

serv_slider4 = [
  'images/serv-slider4/1.png' ,
  'images/serv-slider4/2.png' ,
  'images/serv-slider4/3.png' ,
  'images/serv-slider4/2.png' ,
]
# This function generates the URL for serving static files like images
@galary.app_template_filter('static')
def static_filter(filename):
    return url_for('static', filename=filename)
