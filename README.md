# Parallel_Processing



















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



------------------برای راحتی استفاده از نام توابع که به صورت انگلیسی است بقیه گزارش را به زبان انگلیسی ارائه می دهم-------------------------


## Pro_5
## Scenario 1: Default Output
In this scenario, we use a class MyProcess that inherits from multiprocessing.Process. This class overrides the run method to print a message indicating which process is executing. In each iteration of the loop, an instance of this class is created, started, and then joined to the main process.

## Scenario 2: Printing Additional Information
In this scenario, we utilize the MyProcessWithInfo class, which also inherits from multiprocessing.Process. Within this class, the run method is overridden to print a message containing the process name and its PID (Process ID). Similar to Scenario 1, multiple instances of this class are created, started, and joined in each iteration of the loop.

## Scenario 3: Custom Process Names and Additional Message
This scenario involves the CustomNameProcess class, inheriting from multiprocessing.Process. It accepts a name parameter in its __init__ method to set a custom process name. In the run method, a message is printed displaying the process name along with a custom message. Multiple instances of this class with different names are created, started, and joined in each iteration of the loop.

## Pro_6
## Scenario 1: Default Output
In this scenario, we have a producer-consumer setup using multiprocessing in Python. The Producer class generates random integer items and puts them into a shared queue. Each item is printed with the producer's name and the current queue size. The Consumer class continuously checks the queue for items. If the queue is not empty, it retrieves an item, prints it with the consumer's name, and then sleeps for a short interval.

## Scenario 2: Adjusted Consumer Wait Time
This scenario extends Scenario 1 by modifying the Consumer behavior. The Consumer now waits longer between checking the queue for items, simulating a scenario where consumers process items less frequently than producers generate them. This adjustment demonstrates how different consumer behaviors can impact the processing of items in a shared queue.

## Scenario 3: Multiple Producers and One Consumer
In this scenario, we introduce multiple producers (Producer instances) generating items into the shared queue. Similarly to Scenario 1, each item's addition is logged with the producer's name and the current queue size. The Consumer class consumes items from the queue, printing each item's consumption with its own name. This setup illustrates how multiple producers can concurrently add items to a single queue, managed by a single consumer.

## Pro_7
## Scenario 1: Two Processes with Barrier
In Scenario 1, we create two processes using the Barrier and Lock from the multiprocessing module. The test_with_barrier function demonstrates synchronized execution between two processes using Barrier. Each process waits for the other to reach the barrier before printing a timestamped message using a shared Lock to ensure thread-safe printing. Two additional processes run concurrently without the use of barriers, illustrating unsynchronized execution.

## Scenario 2: Three Processes with Barrier
Scenario 2 extends Scenario 1 by introducing a third process. This setup demonstrates how Barrier with a higher threshold (3 processes) delays execution until all three processes have reached the barrier. Similar to Scenario 1, a Lock ensures thread-safe printing in synchronized processes, while one process operates without synchronization.

## Scenario 3: Four Processes with Barrier
Scenario 3 involves four processes, all using Barrier for synchronization. Each process in this scenario waits for all others to reach the barrier before proceeding, ensuring coordinated execution. A Lock ensures safe access to shared resources during synchronized operations. This scenario showcases the scalability of using barriers in multiprocessing for coordinated task execution

## Pro_8
## Scenario 1: Squaring Numbers
In Scenario 1, a pool of 4 processes is used to square numbers ranging from 0 to 100 concurrently. Each number is squared using the function_square function, and the results are collected using pool.map. The pool is closed and joined to ensure proper cleanup.


## Scenario 2: Cubing Numbers
Scenario 2 involves cubing numbers from 0 to 33 using a pool of 4 processes. The function_cube function calculates the cube of each number, and the results are gathered using pool.map. The pool is then closed and joined to synchronize and collect results.

## Scenario 3: Doubling Numbers
Scenario 3 demonstrates doubling numbers from 0 to 50 in parallel. A pool of 4 processes applies the function_double function to each input, and pool.map gathers the results. Similar to other scenarios, the pool is properly closed and joined after processing.

## Tr_1
## Scenario 1: 
This scenario demonstrates sequential execution using threading in Python. Ten threads are created, each invoking my_func_scenario_1, which simply prints a message indicating its thread number. Each thread is started and immediately joined, ensuring that each completes before the next one begins. This sequential approach guarantees that each thread's function call completes in order, one after the other.

## Scenario 2:
 In contrast to Scenario 1, Scenario 2 showcases concurrent execution with a slight delay before starting each thread. Similar to Scenario 1, ten threads are created using my_func_scenario_2, which prints a unique message including its thread number. However, a small delay of 0.1 seconds is introduced between starting each thread using time.sleep(0.1). This delay allows for some concurrency in starting threads, meaning they may overlap in execution time but still maintain their individual starting points.

## Scenario 3: 
This scenario demonstrates immediate concurrent execution with randomized delays in output. Ten threads are initiated using my_func_scenario_3, where each thread prints its number and a randomly generated delay between 0.1 to 1.0 seconds. These delays simulate real-world scenarios where thread execution times can vary. Despite the delays, all threads are started concurrently, meaning they run simultaneously and independently of each other after being initiated.

## Tr_2
## Scenario 1: Sequential Execution with Modified Message
This scenario demonstrates sequential execution of three functions (function_A, function_B, function_C) using threads. Each function prints a starting message, waits for 2 seconds using time.sleep(2), and then prints an exiting message. Each thread is started sequentially using .start() and .join(), ensuring that one function completes execution before the next one starts.

## Scenario 2: Concurrent Execution with Different Sleep Times
In this scenario, three functions (function_A_diff_sleep, function_B_diff_sleep, function_C_diff_sleep) are executed concurrently using threads. Each function has a different sleep duration: 1 second, 2 seconds, and 3 seconds respectively. Threads are started concurrently with .start() and then joined sequentially with .join(). This allows for overlapping execution where threads with shorter sleep times may complete before those with longer sleep times.

## Scenario 3: Immediate Concurrent Execution with Randomized Output Message
This scenario demonstrates immediate concurrent execution of three functions (function_A_random, function_B_random, function_C_random) using threads. Each function has a randomized sleep duration between 1 to 2 seconds (random.uniform(1, 2)). Threads are started concurrently and then joined sequentially. This scenario showcases concurrent execution where each thread's output message is randomized due to the random sleep duration.

## Tr_3
## Scenario1: Ordered Start with Randomized Sleep
This scenario involves creating 9 threads (MyThread) where each thread sleeps for a random duration between 1 to 3 seconds and then completes. Threads are started sequentially and joined in the order they were created, ensuring that each thread's execution is completed before moving to the next thread. The process ID (os.getpid()) is printed to show which process each thread belongs to.

## Scenario 2: Concurrent Start with Fixed Sleep
In this scenario, 9 threads (MyThreadFixedSleep) are created, each of which sleeps for a fixed duration of 2 seconds. Threads are started concurrently using .start() and then joined sequentially using .join(). This demonstrates concurrent thread execution where each thread performs the same task (sleeping for 2 seconds) independently.

## Scenario 3: Sequential Start with Increasing Sleep Time
Here, 9 threads (MyThreadIncreasingSleep) are created, each with an increasing sleep time ranging from 1 second to 9 seconds (corresponding to their thread ID). Threads are started sequentially and joined immediately after starting using t.join(). This scenario showcases sequential thread execution with increasing sleep times, allowing each subsequent thread to start only after the previous one has completed.

## Tr_4
## Scenario1:
This scenario (sequential) ensures threads acquire and release a lock (threadLock) before printing and sleeping. This guarantees sequential output due to the lock, which prevents threads from interleaving their print statements.

## Scenario2:
In this scenario (concurrent), threads execute without acquiring a lock, allowing them to print and sleep concurrently. This results in potential interleaving of output statements from different threads.

## Scenario3:
This scenario (new_locking_scenario) introduces a new locking mechanism where threads acquire a lock before printing and sleeping. This ensures that each thread completes its execution segment atomically, avoiding interleaving output.

## Tr_5

## Scenario1:
Demonstrates thread-safe operations (add and remove methods) using a RLock in the Box class. Threads add_items and remove_items execute with different rates of item addition and removal, ensuring synchronization through locking.

## Scenario2:
Similar to Scenario 1 but with different sleep times (0.05 seconds for adding and 0.2 seconds for removing). This variation showcases how threads can perform operations with different timings while still maintaining synchronization.

## Scenario3:
Uses the Box class directly with adder and remover functions, demonstrating thread-safe operations on a shared Box instance using threading.

## Tr_6

## Scenario1:
Demonstrates multiple producers generating random items and a single consumer waiting to consume each produced item using a semaphore and a lock for synchronization.

## Scenario2:
Shows multiple consumers waiting for a single producer to produce an item, after which the producer releases the semaphore for all consumers to consume the same item.

## Scenario3:
 Illustrates multiple producers producing random items concurrently while multiple consumers wait to consume these items using semaphore-based synchronization and a lock for item access control.

 ## Tr_7

 ## Scenario1:
 Demonstrates three participants (Dewey, Huey, Louie) starting the race at different times and waiting at a barrier until all participants have reached it.

 ## Scenario2:
 Similar to Scenario 1 but with different participants reaching the barrier in a different order due to varied sleep times, showcasing the flexibility of threading.Barrier.

 ## Scenario3:
 Similar to Scenario 1 but with different participants reaching the barrier in a different order due to varied sleep times, showcasing the flexibility of threading.Barrier.




