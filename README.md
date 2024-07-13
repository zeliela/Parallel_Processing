# Parallel_Processing


## مستندات پروژه FastAPI
## 1.
در این پروژه، من یک API با استفاده از FastAPI پیاده‌سازی کرده‌ام که اسکریپت‌های پایتون مختلف را اجرا می‌کند و خروجی آن‌ها را در قالب JSON ارائه می‌دهد. این API می‌تواند ورودی‌ها را از طریق مسیر (path)، پرس‌وجو (query) و بدنه (body) دریافت کند.

## یک نمونه از FastAPI و Jinja2Templates ایجاد کرده‌ام:
![image](https://github.com/user-attachments/assets/7587dabb-9703-4ae6-ab9d-e4b0e1a7b66d)












این پروژه شامل چندین پوشه با سناریوهای مختلف برای پردازش موازی است. هر پوشه شامل سه سناریو است.

## ساختار پروژه

### پوشه‌های اصلی

- `Pro_1` تا `Pro_8`:Process-Based Parallelism

- `Thr_1` تا `Thr_7`:Thread-Based Parallelism

### هر پوشه شامل فایل‌های زیر است:

- `scenario1.py`: سناریوی اول.
- `scenario2.py`: سناریوی دوم.
- `scenario3.py`: سناریوی سوم.

## توضیحات سناریوها

## Pro_1
## سناریو 1: اجرای متوالی فرآیندها

در این سناریو، فرآیندها به ترتیب و به صورت متوالی اجرا می‌شوند. هر فرآیند منتظر می‌ماند تا فرآیند قبلی به اتمام برسد و سپس شروع به کار می‌کند. این کار به کمک `process.join()` انجام می‌شود تا اطمینان حاصل شود که هر فرآیند پس از تکمیل فرآیند قبلی آغاز می‌شود.

## سناریو 2: اجرای همزمان فرآیندها

در این سناریو، فرآیندها به صورت همزمان اجرا می‌شوند. همه فرآیندها بلافاصله پس از آغاز شروع به کار می‌کنند بدون اینکه منتظر تکمیل فرآیندهای دیگر باشند. این کار به کمک `multiprocessing.Process` و `process.join()` برای هر فرآیند انجام می‌شود تا اطمینان حاصل شود که هر فرآیند به صورت مستقل اجرا می‌شود.

## سناریو 3: اجرای متقارن فرآیندها

در این سناریو، فرآیندها به صورت متقارن و همزمان اجرا می‌شوند، اما با این تفاوت که هر دو فرآیند به طور همزمان شروع می‌شوند و سپس فقط فرآیندهای باقی‌مانده که هنوز در حال اجرا هستند توسط `process.join()` مدیریت می‌شوند. این روش باعث می‌شود که فرآیندها به صورت موثرتری اجرا شوند.

## Pro_2
## Scenario 1: اجرای فرآیندها با نام‌های سفارشی

در این سناریو، دو فرآیند با نام‌های سفارشی "myFunc process" و "Process-2" ایجاد و اجرا می‌شوند. فرآیندها به ترتیب نام‌گذاری شده و پس از اجرا منتظر تکمیل همدیگر می‌مانند.

## Scenario 2: اجرای فرآیندها با نام‌های پیش‌فرض

در این سناریو، دو فرآیند با نام‌های پیش‌فرض ایجاد و اجرا می‌شوند. هر فرآیند به طور خودکار توسط کتابخانه `multiprocessing` نام‌گذاری می‌شود و پس از اجرا منتظر تکمیل همدیگر می‌مانند.

## Scenario 3: اجرای فرآیندها با ترکیبی از نام‌های سفارشی و پیش‌فرض

در این سناریو، یک فرآیند با نام سفارشی "myFunc process" و یک فرآیند دیگر با نام پیش‌فرض ایجاد و اجرا می‌شوند. هر دو فرآیند همزمان شروع به کار می‌کنند و پس از اجرا منتظر تکمیل همدیگر می‌مانند.

## Pro_3
## Scenario 1: اجرای فرآیندهای متوالی با نام‌های مشخص

در این سناریو، سه فرآیند با نام‌های مشخص "NO_background_process" و "background_process" ایجاد و اجرا می‌شوند. فرآیندهای "NO_background_process" به صورت متوالی اجرا می‌شوند، در حالی که فرآیند "background_process" به طور همزمان با دومین فرآیند "NO_background_process" اجرا می‌شود.

## Scenario 2: اجرای فرآیندها با تنظیمات مختلف دیمون

در این سناریو، دو فرآیند با نام‌های "background_process" و "NO_background_process" ایجاد و اجرا می‌شوند. فرآیند "background_process" به عنوان یک فرآیند دیمون (Daemon) تنظیم شده است و فرآیند "NO_background_process" به عنوان یک فرآیند عادی (Non-Daemon) اجرا می‌شود. هر دو فرآیند به طور همزمان شروع به کار می‌کنند.

## Scenario 3: تنظیمات مختلف دیمون و تأثیر آن بر رفتار خاتمه

در این سناریو، دو فرآیند با نام‌های "background_process" و "NO_background_process" ایجاد و اجرا می‌شوند. هر دو فرآیند به عنوان فرآیندهای دیمون (Daemon) تنظیم شده‌اند. این تنظیمات باعث می‌شود که در صورت پایان یافتن فرآیند اصلی، فرآیندهای دیمون نیز به طور خودکار خاتمه یابند.

## Pro_4
## Scenario 1:
در این سناریو، یک فرآیند ایجاد و اجرا می‌شود که تابع فو را فراخوانی می‌کند. پس از شروع فرآیند و اجرای چند دستور، فرآیند بلافاصله با استفاده از متد ترمینیت متوقف می‌شود و پس از آن با استفاده از متد جوین به فرآیند اصلی ملحق می‌شود. در نهایت، وضعیت فرآیند و کد خروجی آن چاپ می‌شود.

## Scenario 2:
در این سناریو، یک فرآیند ایجاد و اجرا می‌شود که تابع فو را فراخوانی می‌کند. فرآیند برای دو ثانیه اجرا می‌شود و سپس با استفاده از سیگنال از طریق متد  متوقف می‌شود. بعد از متوقف شدن فرآیند، با استفاده از متد جوین به فرآیند اصلی ملحق می‌شود و وضعیت فرآیند و کد خروجی آن چاپ می‌شود.

## Scenario 3:
. فرآیند برای یک ثانیه متوقف می‌شود و اگر همچنان در حال اجرا باشد، با استفاده از متد ترمینیتت  متوقف می‌شود. سپس فرآیند با استفاده از متد جوین  به فرآیند اصلی ملحق می‌شود و وضعیت فرآیند و کد خروجی آن چاپ می‌شود.


## Pro_5
## Scenario 1:
در این سناریو، ما از کلاسی به نام MyProcess که از multiprocessing.Process ارث‌بری می‌کند، استفاده می‌کنیم. این کلاس متد run را بازنویسی می‌کند تا پیامی را چاپ کند که نشان می‌دهد کدام فرآیند در حال اجرا است. در هر تکرار حلقه، یک نمونه از این کلاس ایجاد، شروع و سپس به فرآیند اصلی پیوسته می‌شود.

## Scenario 2:
در این سناریو، ما از کلاس MyProcessWithInfo که همچنین از multiprocessing.Process ارث‌بری می‌کند، استفاده می‌کنیم. در این کلاس، متد run بازنویسی می‌شود تا پیامی حاوی نام فرآیند و شناسه فرآیند (PID) چاپ کند. مشابه سناریوی 1، چندین نمونه از این کلاس ایجاد، شروع و در هر تکرار حلقه به فرآیند اصلی پیوسته می‌شود.

## Scenario 3:
این سناریو شامل کلاس CustomNameProcess است که از multiprocessing.Process ارث‌بری می‌کند. این کلاس پارامتری به نام name را در متد __init__ خود می‌پذیرد تا نام سفارشی برای فرآیند تنظیم کند. در متد run، پیامی چاپ می‌شود که نام فرآیند و یک پیام سفارشی را نمایش می‌دهد. چندین نمونه از این کلاس با نام‌های مختلف ایجاد، شروع و در هر تکرار حلقه به فرآیند اصلی پیوسته می‌شود.

## Pro_6
## Scenario 1:
در این سناریو، ما یک تنظیم تولیدکننده-مصرف‌کننده با استفاده از multiprocessing در پایتون داریم. کلاس Producer آیتم‌های صحیح تصادفی تولید می‌کند و آن‌ها را در یک صف مشترک قرار می‌دهد. هر آیتم با نام تولیدکننده و اندازه فعلی صف چاپ می‌شود. کلاس Consumer به طور مداوم صف را برای آیتم‌ها بررسی می‌کند. اگر صف خالی نباشد، آیتمی را بازیابی کرده، آن را با نام مصرف‌کننده چاپ می‌کند و سپس برای مدت کوتاهی می‌خوابد.

## Scenario 2:
این سناریو سناریوی 1 را با تغییر رفتار مصرف‌کننده گسترش می‌دهد. اکنون مصرف‌کننده زمان بیشتری بین بررسی صف برای آیتم‌ها صبر می‌کند، شبیه‌سازی سناریویی که در آن مصرف‌کنندگان آیتم‌ها را کمتر از تولیدکنندگان تولید می‌کنند. این تنظیم نشان می‌دهد که چگونه رفتارهای مختلف مصرف‌کننده می‌تواند بر پردازش آیتم‌ها در یک صف مشترک تأثیر بگذارد.

## Scenario 3:
در این سناریو، چندین تولیدکننده (نمونه‌های Producer) را معرفی می‌کنیم که آیتم‌ها را به صف مشترک اضافه می‌کنند. مشابه سناریوی 1، افزودن هر آیتم با نام تولیدکننده و اندازه فعلی صف ثبت می‌شود. کلاس Consumer آیتم‌ها را از صف مصرف می‌کند و مصرف هر آیتم را با نام خود چاپ می‌کند. این تنظیم نشان می‌دهد که چگونه چندین تولیدکننده می‌توانند به صورت همزمان آیتم‌ها را به یک صف اضافه کنند که توسط یک مصرف‌کننده مدیریت می‌شود.

## Pro_7
## Scenario 1:
در سناریو 1، ما دو فرآیند با استفاده از Barrier و Lock از ماژول multiprocessing ایجاد می‌کنیم. تابع test_with_barrier اجرای همزمان بین دو فرآیند را با استفاده از Barrier نشان می‌دهد. هر فرآیند منتظر می‌ماند تا فرآیند دیگر به مانع برسد قبل از چاپ یک پیام زمان‌دار با استفاده از یک Lock مشترک برای اطمینان از چاپ ایمن. دو فرآیند اضافی به طور همزمان بدون استفاده از موانع اجرا می‌شوند، نشان می‌دهد که چگونه بدون همزمان‌سازی عمل می‌کنند.

## Scenario 2:
سناریو 2 سناریو 1 را با معرفی یک فرآیند سوم گسترش می‌دهد. این تنظیم نشان می‌دهد که چگونه Barrier با آستانه بالاتر (3 فرآیند) اجرای فرآیندها را تا زمانی که هر سه فرآیند به مانع نرسیده‌اند، به تأخیر می‌اندازد. مشابه سناریو 1، یک Lock اطمینان حاصل می‌کند که چاپ در فرآیندهای همزمان به صورت ایمن انجام می‌شود، در حالی که یک فرآیند بدون همزمان‌سازی عمل می‌کند.

## Scenario 3:
سناریو 3 شامل چهار فرآیند است که همگی برای همزمان‌سازی از Barrier استفاده می‌کنند. هر فرآیند در این سناریو منتظر می‌ماند تا همه فرآیندهای دیگر به مانع برسند، و سپس ادامه می‌دهد، اطمینان از اجرای هماهنگ فرآیندها. یک Lock دسترسی ایمن به منابع مشترک را در عملیات‌های همزمان تضمین می‌کند. این سناریو نشان می‌دهد که چگونه استفاده از موانع در پردازش موازی برای اجرای هماهنگ وظایف مقیاس‌پذیر است.

## Pro_8
## Scenario 1:
در سناریو 1، از یک استخر شامل 4 فرآیند برای محاسبه توان دوم اعداد از 0 تا 100 به طور همزمان استفاده می‌شود. هر عدد با استفاده از تابع function_square به توان دوم می‌رسد و نتایج با استفاده از pool.map جمع‌آوری می‌شود. استخر بسته شده و به فرآیند اصلی ملحق می‌شود تا اطمینان حاصل شود که به درستی پاک‌سازی انجام می‌شود.

## Scenario 2:
سناریو 2 شامل محاسبه توان سوم اعداد از 0 تا 33 با استفاده از یک استخر شامل 4 فرآیند است. تابع function_cube توان سوم هر عدد را محاسبه می‌کند و نتایج با استفاده از pool.map جمع‌آوری می‌شود. استخر سپس بسته شده و به فرآیند اصلی ملحق می‌شود تا نتایج به درستی همگام‌سازی و جمع‌آوری شوند.

## Scenario 2:
سناریو 3 دو برابر کردن اعداد از 0 تا 50 را به صورت موازی نشان می‌دهد. یک استخر شامل 4 فرآیند تابع function_double را بر روی هر ورودی اعمال می‌کند و pool.map نتایج را جمع‌آوری می‌کند. مشابه سناریوهای دیگر، استخر پس از پردازش به درستی بسته شده و به فرآیند اصلی ملحق می‌شود.


## Tr_1
## Scenario 1:
این سناریو اجرای ترتیبی با استفاده از threading در پایتون را نشان می‌دهد. ده رشته ایجاد می‌شوند که هر کدام my_func_scenario_1 را فراخوانی می‌کنند، که به سادگی پیامی چاپ می‌کند که نشان می‌دهد کدام رشته در حال اجرا است. هر رشته شروع می‌شود و بلافاصله ملحق می‌شود، اطمینان حاصل می‌شود که هر کدام قبل از شروع بعدی کامل می‌شود. این روش ترتیبی تضمین می‌کند که هر فراخوانی تابع رشته به ترتیب و یکی پس از دیگری تکمیل می‌شود.

## Scenario 2:
در تضاد با سناریو 1، سناریو 2 اجرای همزمان با تاخیر کمی قبل از شروع هر رشته را نشان می‌دهد. مشابه سناریو 1، ده رشته با استفاده از my_func_scenario_2 ایجاد می‌شوند، که پیامی منحصر به فرد حاوی شماره رشته چاپ می‌کند. با این حال، تاخیر کوچکی به مدت 0.1 ثانیه بین شروع هر رشته با استفاده از time.sleep(0.1) معرفی می‌شود. این تاخیر اجازه می‌دهد تا مقداری همزمانی در شروع رشته‌ها وجود داشته باشد، به این معنا که ممکن است آنها در زمان اجرا همپوشانی داشته باشند اما همچنان نقاط شروع جداگانه خود را حفظ می‌کنند.

## Scenario 3:
این سناریو اجرای همزمان فوری با تاخیرهای تصادفی در خروجی را نشان می‌دهد. ده رشته با استفاده از my_func_scenario_3 آغاز می‌شوند، جایی که هر رشته شماره خود و یک تاخیر تصادفی بین 0.1 تا 1.0 ثانیه را چاپ می‌کند. این تاخیرها سناریوهای دنیای واقعی را شبیه‌سازی می‌کنند که در آن زمان‌های اجرای رشته‌ها می‌توانند متفاوت باشند. علیرغم تاخیرها، همه رشته‌ها به صورت همزمان شروع می‌شوند، به این معنا که آنها به طور همزمان و مستقل از یکدیگر پس از شروع اجرا می‌شوند.

## Tr_2
## Scenario 1:
این سناریو اجرای ترتیبی سه تابع (function_A، function_B، function_C) با استفاده از رشته‌ها را نشان می‌دهد. هر تابع یک پیام شروع را چاپ می‌کند، به مدت 2 ثانیه با استفاده از time.sleep(2) منتظر می‌ماند و سپس یک پیام خروج را چاپ می‌کند. هر رشته به طور ترتیبی با استفاده از .start() و .join() شروع می‌شود، اطمینان حاصل می‌شود که یک تابع قبل از شروع تابع بعدی کامل می‌شود.

## Scenario 2:
در این سناریو، سه تابع (function_A_diff_sleep، function_B_diff_sleep، function_C_diff_sleep) به صورت همزمان با استفاده از رشته‌ها اجرا می‌شوند. هر تابع مدت زمان خواب متفاوتی دارد: 1 ثانیه، 2 ثانیه و 3 ثانیه به ترتیب. رشته‌ها به صورت همزمان با .start() شروع می‌شوند و سپس به طور ترتیبی با .join() ملحق می‌شوند. این اجازه می‌دهد تا اجرای همپوشانی که در آن رشته‌هایی با زمان‌های خواب کوتاه‌تر ممکن است قبل از رشته‌هایی با زمان‌های خواب طولانی‌تر کامل شوند.

## Scenario 3:
این سناریو اجرای همزمان فوری سه تابع (function_A_random، function_B_random، function_C_random) با استفاده از رشته‌ها را نشان می‌دهد. هر تابع مدت زمان خواب تصادفی بین 1 تا 2 ثانیه (random.uniform(1, 2)) دارد. رشته‌ها به صورت همزمان شروع می‌شوند و سپس به طور ترتیبی ملحق می‌شوند. این سناریو اجرای همزمان را نشان می‌دهد که در آن پیام خروجی هر رشته به دلیل مدت زمان خواب تصادفی تصادفی است.

## Tr_3
## Scenario 1:
این سناریو شامل ایجاد 9 رشته (MyThread) است که هر رشته برای مدت زمان تصادفی بین 1 تا 3 ثانیه می‌خوابد و سپس کامل می‌شود. رشته‌ها به طور ترتیبی شروع و به ترتیب ایجاد شده ملحق می‌شوند، اطمینان حاصل می‌شود که اجرای هر رشته قبل از حرکت به رشته بعدی کامل می‌شود. شناسه فرآیند (os.getpid()) چاپ می‌شود تا نشان دهد که هر رشته به کدام فرآیند تعلق دارد.

## Scenario 2:
در این سناریو، 9 رشته (MyThreadFixedSleep) ایجاد می‌شوند که هر کدام برای مدت زمان ثابت 2 ثانیه می‌خوابند. رشته‌ها به صورت همزمان با استفاده از .start() شروع می‌شوند و سپس به طور ترتیبی با استفاده از .join() ملحق می‌شوند. این اجرای همزمان رشته‌ها را نشان می‌دهد که در آن هر رشته وظیفه مشابهی (خوابیدن برای 2 ثانیه) را به طور مستقل انجام می‌دهد.

## Scenario 3:
در اینجا، 9 رشته (MyThreadIncreasingSleep) ایجاد می‌شوند که هر کدام زمان خواب افزایشی از 1 ثانیه تا 9 ثانیه (مطابق با شناسه رشته خود) دارند. رشته‌ها به طور ترتیبی شروع و بلافاصله پس از شروع با استفاده از t.join() ملحق می‌شوند. این سناریو اجرای ترتیبی رشته‌ها را با زمان خواب افزایشی نشان می‌دهد، به طوری که هر رشته بعدی تنها پس از کامل شدن رشته قبلی شروع می‌شود.

## Tr_4
## Scenario 1:
این سناریو (ترتیبی) تضمین می‌کند که رشته‌ها قبل از چاپ و خوابیدن یک قفل (threadLock) را دریافت و آزاد می‌کنند. این تضمین خروجی ترتیبی به دلیل قفل را می‌دهد که مانع از تداخل عبارات چاپی رشته‌ها می‌شود.

## Scenario 2:
در این سناریو (همزمان)، رشته‌ها بدون دریافت یک قفل اجرا می‌شوند و به آنها اجازه می‌دهد تا به طور همزمان چاپ و خواب کنند. این منجر به تداخل احتمالی عبارات خروجی از رشته‌های مختلف می‌شود.

## Scenario 3:
این سناریو (new_locking_scenario) یک مکانیزم قفل جدید معرفی می‌کند که در آن رشته‌ها قبل از چاپ و خوابیدن یک قفل دریافت می‌کنند. این تضمین می‌کند که هر رشته بخش اجرای خود را به صورت اتمی کامل می‌کند و از تداخل خروجی جلوگیری می‌کند.

## Tr_5
## Scenario 1:
عملیات‌های ایمن رشته‌ای (روش‌های add و remove) با استفاده از RLock در کلاس Box را نشان می‌دهد. رشته‌های add_items و remove_items با نرخ‌های مختلف اضافه و حذف آیتم‌ها اجرا می‌شوند و از طریق قفل‌گذاری همگام‌سازی را تضمین می‌کنند.

## Scenario 2=
مشابه سناریو 1 اما با زمان‌های خواب متفاوت (0.05 ثانیه برای اضافه کردن و 0.2 ثانیه برای حذف). این واریاسیون نشان می‌دهد که چگونه رشته‌ها می‌توانند عملیات‌ها را با زمان‌های مختلف انجام دهند در حالی که همچنان همگام‌سازی را حفظ می‌کنند.

## Scenario 3:
استفاده از کلاس Box به طور مستقیم با توابع adder و remover، عملیات‌های ایمن رشته‌ای روی یک نمونه Box مشترک با استفاده از threading را نشان می‌دهد.

## Tr_6
## Scenario 1:
تولیدکنندگان متعدد تولید آیتم‌های تصادفی و یک مصرف‌کننده که منتظر مصرف هر آیتم تولید شده است با استفاده از semaphore و یک قفل برای همگام‌سازی را نشان می‌دهد.

## Scenario 2:
چندین مصرف‌کننده که منتظر تولید یک آیتم از یک تولیدکننده هستند، پس از آن تولیدکننده semaphore را برای همه مصرف‌کنندگان آزاد می‌کند تا همان آیتم را مصرف کنند را نشان می‌دهد.

## Scenario 3:
تولیدکنندگان متعدد به طور همزمان آیتم‌های تصادفی تولید می‌کنند در حالی که چندین مصرف‌کننده منتظر مصرف این آیتم‌ها هستند با استفاده از همگام‌سازی مبتنی بر semaphore و یک قفل برای کنترل دسترسی به آیتم را نشان می‌دهد.

## Tr_7
## Scenario 1:
سه شرکت‌کننده (Dewey، Huey، Louie) را نشان می‌دهد که در زمان‌های مختلف شروع به مسابقه می‌کنند و در یک مانع منتظر می‌مانند تا همه شرکت‌کنندگان به آن برسند.

## Scenario 2:
مشابه سناریو 1 اما با شرکت‌کنندگان مختلفی که به دلیل زمان‌های خواب متفاوت به ترتیب مختلف به مانع می‌رسند، انعطاف‌پذیری threading.Barrier را نشان می‌دهد.

## Scenario 3:
مشابه سناریو 1 اما با شرکت‌کنندگان مختلفی که به دلیل زمان‌های خواب متفاوت به ترتیب مختلف به مانع می‌رسند، انعطاف‌پذیری threading.Barrier را نشان می‌دهد.





