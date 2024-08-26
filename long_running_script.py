import time

def main():
    print("Starting long-running task...")
    for i in range (10):
        print(f"Minute {i+1}")
        time.sleep(10)
    print("Task completed")

if __name__ == "__main__":
    main()
