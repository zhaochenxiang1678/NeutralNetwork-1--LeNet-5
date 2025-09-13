import onnx

try:
    # 1. 加载你的 ONNX 模型
    onnx_model = onnx.load("lenet.onnx")

    # 2. 直接打印加载后的模型对象即可
    print("=========== ONNX 模型结构 (推荐方法) ===========")
    print(onnx_model)
    print("=================================================")

except FileNotFoundError:
    print("错误：找不到 'lenet.onnx' 文件。")
except Exception as e:
    print(f"打开或解析模型时发生错误: {e}")