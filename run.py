import uvicorn

uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="debug", debug=True,
                workers=1, limit_concurrency=1, limit_max_requests=1)