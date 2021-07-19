# CCCAM Scrapper

* **Build**. Run the following command inside the folder with the Dockerfile
```
docker build -t vmartinvega-pivotal/sky-planner .
```
* **Push**. Run the following command inside the folder with the Dockerfile
```
docker push vmartinvega-pivotal/sky-planner
```

* **Run locally**.
```
docker run -e API_KEY= \
 -it --rm vmartinvega-pivotal/sky-planner
```
