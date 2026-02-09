import threading
import time
from typing import List

# Thread-safe storage for results
results_lock = threading.Lock()
thread_results = []

def compute_gwa_thread(subject_name: str, grade: float, thread_id: int):
    """
    Compute GWA for a single subject using threading.
    
    Args:
        subject_name: Name of the subject
        grade: Grade value
        thread_id: Identifier for the thread
    """
    # Simulates processing time
    time.sleep(0.01)
    
    # Calculate GWA (in this case, just the grade itself for individual subjects)
    gwa = grade
    
    # Thread-safe result storage
    with results_lock:
        thread_results.append({
            'subject': subject_name,
            'grade': grade,
            'thread_id': thread_id
        })
        print(f"[Thread-{thread_id}] {subject_name}: {grade:.2f}")

def get_user_input() -> List[tuple]:
    """
    Get grades from user input in a creative and user-friendly way.
    
    Returns:
        List of tuples containing (subject_name, grade)
    """
    print("=" * 60)
    print("GRADE COMPUTING SYSTEM - Multithreading Version")
    print("=" * 60)
    
    subjects = []
    
    num_subjects = int(input("\nHow many subjects do you want to enter? "))
    
    for i in range(num_subjects):
        print(f"\n--- Subject {i+1} ---")
        subject_name = input("Subject name: ")
        while True:
            try:
                grade = float(input(f"Grade for {subject_name}: "))
                if 0 <= grade <= 100:
                    subjects.append((subject_name, grade))
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
    
    return subjects

def calculate_overall_gwa(grades: List[float]) -> float:
    """Calculate the overall GWA from all grades."""
    return sum(grades) / len(grades) if grades else 0

def main():
    """Main execution function for multithreading approach."""
    # Get user input
    subjects = get_user_input()
    
    if not subjects:
        print("No subjects entered!")
        return
    
    print("\n" + "=" * 60)
    print("Processing grades using MULTITHREADING...")
    print("=" * 60 + "\n")
    
    # Start timing
    start_time = time.time()
    
    # Create and start threads
    threads = []
    global thread_results
    thread_results = []  # Reset results
    
    for idx, (subject_name, grade) in enumerate(subjects):
        thread = threading.Thread(
            target=compute_gwa_thread,
            args=(subject_name, grade, idx + 1)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # End timing
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Calculate overall GWA
    all_grades = [grade for _, grade in subjects]
    overall_gwa = calculate_overall_gwa(all_grades)
    
    # Display results
    print("\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"\nTotal Subjects: {len(subjects)}")
    print(f"Overall GWA: {overall_gwa:.2f}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print("\n" + "=" * 60)
    
    return execution_time, overall_gwa


if __name__ == "__main__":
    main()
 