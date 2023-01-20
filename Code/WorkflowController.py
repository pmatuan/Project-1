import base64

class WorkflowController:
    def __init__(self, repo):
        self.repo = repo

    # Xem trạng thái workflow mới nhất của repo
    def stateOfPipeline(self):
        pipeline = self.repo.pipelines.list()[0]
        if pipeline.status == 'failed':
            for job in pipeline.jobs.list():
                if job.status == 'failed':
                    print(f"Job: {job.name} failed")
                    print(f"Job Web URL: {job.web_url}")

    # Lấy file .gitlab-ci.yml
    def getConfig(self):
        ci_config = self.repo.files.get(file_path='.gitlab-ci.yml', ref='main')
        content = base64.b64decode(ci_config.content).decode("utf-8")
        content = content.replace('\\n', '\n')
        return content

    # Sửa file .gitlab-ci.yml
    def editConfig(self):
        pass

    # Tạo pipeline !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def createPipeline(self):
        pipeline = self.repo.pipelines.create({'ref': 'main'})
        print('Create pipeline successfully')
        return pipeline

    # Chạy pipeline: có vẻ đang thừa, vì khi create nó tự chạy
    def runPipeline(self, pipeline):
        # ?
        pipeline.play()

    # Hủy pipeline
    def cancelPipeline(self, pipeline):
        pipeline.cancel()
        print('Cancelled pipeline successfully')

    def historyPipeline(self):
        pipelines = self.repo.pipelines.list()
        for pipeline in pipelines:
            print("Pipeline ID: ", pipeline.attributes['id'])
            print("Ref: ", pipeline.attributes['ref'])
            print("Status: ", pipeline.attributes['status'])
            print("------")
