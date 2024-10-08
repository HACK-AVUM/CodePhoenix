import subprocess
import os
import sys


def check_sonarscanner_installed():
    """Verifica se SonarScanner è installato e accessibile."""
    try:
        result = subprocess.run(['sonar-scanner', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"SonarScanner installato: {result.stdout.splitlines()[0]}")
        else:
            print("SonarScanner non trovato. Assicurati che sia installato e aggiunto al PATH.")
            sys.exit(1)
    except FileNotFoundError:
        print("SonarScanner non trovato. Assicurati che sia installato e aggiunto al PATH.")
        sys.exit(1)


def run_sonarqube_analysis(project_dir):
    """Esegue l'analisi del codice con SonarScanner."""
    if not os.path.isdir(project_dir):
        print(f"La directory del progetto '{project_dir}' non esiste.")
        sys.exit(1)

    os.chdir(project_dir)
    print(f"Eseguendo SonarScanner nella directory: {project_dir}")

    try:
        result = subprocess.run(['sonar-scanner'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("Errore durante l'esecuzione di SonarScanner:")
            print(result.stderr)
            sys.exit(result.returncode)
        else:
            print("Analisi SonarQube completata con successo.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Uso: python sonarqube_analyzer.py")
        sys.exit(1)

    project_dir = sys.argv[1]
    check_sonarscanner_installed()
    run_sonarqube_analysis(project_dir)


if __name__ == "__main__":
    main()