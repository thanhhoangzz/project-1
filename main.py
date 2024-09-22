from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Tạo layout theo chiều dọc
        layout = BoxLayout(orientation='vertical')
        
        # Tạo một nút bấm với dòng chữ
        btn = Button(text="Nhấn vào đây!", font_size=30)
        
        # Kết nối sự kiện nhấn nút với hàm xử lý
        btn.bind(on_press=self.on_button_press)
        
        # Thêm nút vào layout
        layout.add_widget(btn)
        
        return layout

    def on_button_press(self, instance):
        # Khi nút được nhấn, thay đổi văn bản của nút
        instance.text = "Bạn đã nhấn vào tôi!"

# Khởi chạy ứng dụng
if __name__ == '__main__':
    MyApp().run()
