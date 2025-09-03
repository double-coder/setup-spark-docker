FROM bitnami/spark:latest

# Install any additional dependencies here
# For example:
# RUN apt-get update && apt-get install -y --no-install-recommends some-package
RUN pip install findspark
