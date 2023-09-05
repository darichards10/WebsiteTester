import csv

def generate_locust_script(input_csv, output_script):
    urls = []

    with open(input_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) 
        for row in reader:
            if row:
                urls.append(row[0])

    with open(output_script, 'w') as script_file:
        script_file.write("from locust import HttpUser, task, between\n\n")
        script_file.write("class MyUser(HttpUser):\n")
        script_file.write("    wait_time = between(1, 2)\n\n")
        
        for i, url in enumerate(urls):
            script_file.write(f"    @task\n")
            script_file.write(f"    def task_{i}(self):\n")
            script_file.write(f"        self.client.get('{url}')\n\n")

if __name__ == "__main__":
    input_csv = "sitetestresults.csv"       
    output_script = "load_test.py"  
    generate_locust_script(input_csv, output_script)