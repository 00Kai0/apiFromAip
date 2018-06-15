class Filter(object):
    '''
    基础筛选器
    '''

    def __init__(self, data, ai_model):
        self.data = data
        self.ai_model = ai_model

    def filter(self):
        '''
        筛选函数,筛选模式由ai_model决定
        '''
        pass

    def isError(self):
        '''
        鉴别接收的数据是否包含错误码
        返回布尔类型
        '''
        error_code = self.data.get('error_code', None)
        if error_code is None or error_code == 0:
            # 结果无误，返回False
            return False
        else:
            return True


class Img_classifyFilter(Filter):
    '''
    图像识别筛选器
    '''

    def __init__(self, data, ai_model):
        super(Img_classifyFilter, self).__init__(data, ai_model)

    def topResult(self, results, score_key):
        '''
        筛选最可信结果
        '''
        topput = dict()
        topput[score_key] = -1
        for temp in results:
            try:
                if topput[score_key] < temp[score_key]:
                    topput = temp
            except TypeError:
                # 部分返回的置信度数据可能是以字符串形式，这里捕获该异常
                if float(topput[score_key]) < float(temp[score_key]):
                    topput = temp
        return topput

    def filter(self):
        '''
        图像筛选函数
        定制化图像识别暂不支持，筛选模式错误,返回原始数据
        '''

        # 如果数据中含有效错误码，返回原始数据
        if self.isError():
            return self.data

        # 根据筛选模式筛选数据
        if self.ai_model == "object_detect":
            result = self.data["result"]
            output = dict()
            output["宽度"] = result["width"]
            output["高度"] = result["height"]
            output["垂直坐标"] = result["top"]
            output["水平坐标"] = result["left"]
        elif self.ai_model == "car":
            result = self.data["result"]
            topput = self.topResult(result, "score")
            output = dict()
            output["车型"] = topput["name"]
            output["年份信息"] = topput["year"]
            output["颜色"] = self.data["color_result"]
        elif self.ai_model == "dish":
            result = self.data["result"]
            topput = self.topResult(result, "probability")
            output = dict()
            output["菜名"] = topput["name"]
            output["卡路里"] = topput["calorie"]
        elif self.ai_model == "logo":
            result = self.data["result"]
            topput = self.topResult(result, "probability")
            output = dict()
            output["LOGO名"] = topput["name"]
        elif self.ai_model == "animal":
            result = self.data["result"]
            topput = self.topResult(result, "score")
            output = dict()
            output["动物名"] = topput["name"]
        elif self.ai_model == "plant":
            result = self.data["result"]
            topput = self.topResult(result, "score")
            output = dict()
            output["植物名"] = topput["name"]
        elif self.ai_model == "advanced_general":
            result = self.data["result"]
            topput = self.topResult(result, "score")
            output = dict()
            output["分类"] = topput["root"]
            output["物品名"] = topput["keyword"]
        elif self.ai_model == "customized_image":
            output = self.data
        elif self.ai_model == "customized_object":
            output = self.data
        else:
            output = self.data
        return output


class OcrFilter(Filter):
    '''
    文字识别筛选器
    '''

    def __init__(self, data, ai_model):
        super(OcrFilter, self).__init__(data, ai_model)

    def filter(self):
        '''
        文字识别筛选函数
        暂支持通用文字识别,筛选模式错误返回原始数据
        '''
        # 含有效错误码，返回原始数据
        if self.isError():
            return self.data

        # 根据筛选模式筛选数据
        if self.ai_model == "general_basic":
            words_result = self.data["words_result"]
            output = {"result": ""}
            if words_result[0].get("probability") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + "\n"
            else:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + str(temp["probability"]["average"]) + ")\n"
        elif self.ai_model == "accurate_basic":
            words_result = self.data["words_result"]
            output = {"result": ""}
            if words_result[0].get("probability") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + "\n"
            else:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + str(temp["probability"]["average"]) + ")\n"
        elif self.ai_model == "general":
            words_result = self.data["words_result"]
            output = {"result": ""}
            if words_result[0].get("probability") is None and words_result[0].get("location") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + "\n"
            elif words_result[0].get("probability") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + \
                        str(temp["location"]["left"]) + "," + str(temp["location"]["top"]) + "," + str(temp["location"]["width"]) + "," +\
                        str(temp["location"]["height"]) + ")\n"
            elif words_result[0].get("location") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + str(temp["probability"]["average"]) + ")\n"
            else:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + str(temp["probability"]["average"]) + ") (" + \
                        str(temp["location"]["left"]) + "," + str(temp["location"]["top"]) + "," + str(temp["location"]["width"]) + "," +\
                        str(temp["location"]["height"]) + ")\n"
        elif self.ai_model == "accurate":
            words_result = self.data["words_result"]
            output = {"result": ""}
            if words_result[0].get("probability") is None and words_result[0].get("location") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + "\n"
            elif words_result[0].get("probability") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + \
                        str(temp["location"]["left"]) + "," + str(temp["location"]["top"]) + "," + str(temp["location"]["width"]) + "," +\
                        str(temp["location"]["height"]) + ")\n"
            elif words_result[0].get("location") is None:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + str(temp["probability"]["average"]) + ")\n"
            else:
                for temp in words_result:
                    output["result"] = output["result"] + temp["words"] + " (" + str(temp["probability"]["average"]) + ") (" + \
                        str(temp["location"]["left"]) + "," + str(temp["location"]["top"]) + "," + str(temp["location"]["width"]) + "," +\
                        str(temp["location"]["height"]) + ")\n"
        elif self.ai_model == "general_enhanced":
            output = self.data
        else:
            output = self.data
        return output


class FaceFilter(Filter):
    '''
    人脸识别筛选器
    '''

    def __init__(self, data, ai_model):
        super(FaceFilter, self).__init__(data, ai_model)

    class FaceData(object):
        '''
        处理人脸选填信息类
        用于处理非必要信息
        '''

        def __init__(self, face):
            self.face = face
            # 各类信息的英译中对应
            self.ftype_tran = {"human": "真实人脸", "cartoon": "卡通人脸"}
            self.fshape_tran = {"square": "方形", "triangle": "三角形", "oval": "椭圆", "heart": "心形", "round": "圆形"}
            self.fexpression_tran = {"none": "不笑", "smile": "微笑", "laugh": "大笑"}
            self.fgender_tran = {"male": "男性", "female": "女性"}
            self.fglasses_tran = {"none": "无眼镜", "common": "普通眼镜", "sun": "墨镜"}
            self.frace_tran = {"yellow": "黄种人", "white": "白种人", "black": "黑种人", "arabs": "阿拉伯人"}

        '''
        获取各种选填信息的函数，不存在时抛出异常并返回None
        '''

        def get_face_type(self):
            try:
                face_type = self.face["face_type"]["type"]
                face_type = self.ftype_tran[face_type]
            except KeyError:
                return None
            return face_type

        def get_age(self):
            try:
                age = self.face["age"]
            except KeyError:
                return None
            return age

        def get_beauty(self):
            try:
                beauty = self.face["beauty"]
            except KeyError:
                return None
            return beauty

        def get_expression(self):
            try:
                expression = self.face["expression"]["type"]
                expression = self.fexpression_tran[expression]
            except KeyError:
                return None
            return expression

        def get_face_shape(self):
            try:
                face_shape = self.face["face_shape"]["type"]
                face_shape = self.fshape_tran[face_shape]
            except KeyError:
                return None
            return face_shape

        def get_gender(self):
            try:
                gender = self.face["gender"]["type"]
                gender = self.fgender_tran[gender]
            except KeyError:
                return None
            return gender

        def get_glasses(self):
            try:
                glasses = self.face["glasses"]["type"]
                glasses = self.fglasses_tran[glasses]
            except KeyError:
                return None
            return glasses

        def get_race(self):
            try:
                race = self.face["race"]["type"]
                race = self.frace_tran[race]
            except KeyError:
                return None
            return race

    def get_extraData(self, face):
        '''
        获取人脸识别获得的可选信息
        '''
        facedata = self.FaceData(face)
        outface = dict()
        if facedata.get_face_type():
            outface["人脸类型"] = facedata.get_face_type()
        if facedata.get_face_shape():
            outface["脸型"] = facedata.get_face_shape()
        if facedata.get_age():
            outface["年龄"] = facedata.get_age()
        if facedata.get_beauty():
            outface["美丑打分"] = facedata.get_beauty()
        if facedata.get_expression():
            outface["表情"] = facedata.get_expression()
        if facedata.get_gender():
            outface["性别"] = facedata.get_gender()
        if facedata.get_glasses():
            outface["眼镜"] = facedata.get_glasses()
        if facedata.get_race():
            outface["人种"] = facedata.get_race()
        return outface

    def filter(self):
        '''
        人脸识别筛选函数
        筛选模式不正确则返回原始数据
        '''

        # 含有错误码，返回原始数据
        if self.isError():
            return self.data

        # 根据筛选模式筛选数据
        if self.ai_model == "face_detect":
            face_list = self.data["result"]["face_list"]
            result = list()
            for temp in face_list:
                face = self.get_extraData(temp)
                face["人脸位置"] = {"左距": temp["location"]["left"], "上距": temp["location"]["top"],
                                   "宽度": temp["location"]["width"], "高度": temp["location"]["height"],
                                   "旋转角度": temp["location"]["rotation"]}
                result.append(face)
            output = {"人脸": result}

        elif self.ai_model == "face_match":
            output = {"相似度得分": self.data["result"]["score"]}
        elif self.ai_model == "face_faceverify":
            face_list = self.data["result"]["face_list"]
            result = list()
            for temp in face_list:
                face = self.get_extraData(temp)
                face["人脸位置"] = {"左距": temp["location"]["left"], "上距": temp["location"]["top"],
                                   "宽度": temp["location"]["width"], "高度": temp["location"]["height"],
                                   "旋转角度": temp["location"]["rotation"]}
                result.append(face)
            output = {"人脸": result, "活体分数值": self.data["result"]["face_liveness"]}
        else:
            output = self.data
        return output
