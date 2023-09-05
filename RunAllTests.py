import subprocess
import sys
import traceback


def run_load_Test(url, users, ramp_up_rate, run_time):
    try:
        subprocess.run(["locust", "-f", "load_test.py", "--csv=test", "--headless", f"--host={url}",'-u', f"{users}",'-r', f"{ramp_up_rate}", '--run-time', f"{run_time}" ], check=True)
        print("Load test completed successfully!")
    except subprocess.CalledProcessError:
        print("An error occurred while running the site test.")
    return 

def run_build_test():
    try:
        subprocess.run(["python", "load_test_file_builder.py"], check=True)
        print("Load test file build completed successfully!")
    except subprocess.CalledProcessError:
        print("An error occurred while running theload test builder.")

def run_site_test(site_name, output_name):
    try:
        subprocess.run(["python", "SiteTester.py", site_name, output_name], check=True)
        print("Site test completed successfully!")
    except subprocess.CalledProcessError:
        print("An error occurred while running the site test.")

def run_report_builder():
    try:
        subprocess.run(["python", "ReportBuilder.py"], check=True)
        print("Report Builder completed successfully!")
    except subprocess.CalledProcessError:
        print("An error occurred while running the report builder.")

if __name__ == "__main__":
    try:
        #python RunAllTests.py -site -users -ramp_up_rate -test_time(seconds)
        run_site_test(str(sys.argv[1]), "sitetestresults.csv")
        run_build_test()
        run_load_Test(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
        run_report_builder()
    except Exception as e:
        print(f"Error - {e}")
        traceback.print_exc()