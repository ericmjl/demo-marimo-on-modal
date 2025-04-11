import modal

image = (
    modal.Image.debian_slim()
    .pip_install(["uv"])
    .add_local_file("protein_estimation.py", "/app/protein_estimation.py", copy=True)
    .workdir("/app")
)

app = modal.App(name="protein-estimation")


@app.function(image=image, allow_concurrent_inputs=100)
@modal.web_server(8000, startup_timeout=60)
def run_protein_estimation():
    import subprocess

    # Port must match the web_server port, and host must be 0.0.0.0 for this to work.
    cmd = "uvx marimo edit protein_estimation.py --sandbox --port 8000 --host 0.0.0.0 --headless --no-token"
    subprocess.Popen(cmd, shell=True)
