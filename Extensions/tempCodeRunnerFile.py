
            if response.ok:
                return response.content
            else:
                sleep(2)
        self.error=True