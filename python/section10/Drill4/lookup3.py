while True:
    print()
    print("---------Từ điển nhân vật Marvel---------")
    print("1.Chọn nhân vật để tra cứu")
    print("2.Thoát")
    user_input = int(input("Sự lựa chọn của bạn : "))
    def lookup():
        key = input("Nhập nhân vật bạn muốn tra cứu :")
        key_half = key.lower()
        key_perfect = key_half.capitalize()
        print(marvel_character[key_perfect])

    if user_input == 1:
        marvel_character = {
        "Iron man": '''Một người tự nhận mình là bác ái, tỉ phú, đào hoa và nhà từ thiện với bộ đồ cơ khí do tự anh ta sáng chế. Downey được phân vai như một phần trong hợp đồng của anh với hãng Marvel, bao gồm Người Sắt 2 và The Avengers. Downey nói rằng anh muốn nhân vật của mình xuất hiện đầu tiên: "Tôi cần ở trong cảnh phim đầu tiên. Tôi không biết anh nghĩ gì nhưng nhân vật của tôi phải làm điều này". Đạo diễn nói: "Thôi được, cứ thử xem". "Chúng tôi đã thử điều này và có vẻ nó không hiệu quả lắm, bởi vì đây là một điều gì đã khác đi, câu chuyện và những ý tưởng là chính, mọi người phải như là một cái xúc tu của con bạch tuộc" - Downey nói. Về sự phát triền tính cách của nhân vật, Downey phát biểu rằng: "Trong Người Sắt 1, đó là một câu chuyện nguyên bản, anh ta mở màn cho sự xuất hiện và tìm lại vị trí của mình, Người Sắt 2 thì không phải là một việc riêng biệt nữa, phải giao tiếp và tạo không gian cho người khác, còn trong The Avengers, anh ấy sẽ bỏ lại những thứ đó''',
        "Captain america": ''' Một cựu chiến binh từ Thế chiến thứ II đã được tăng cường tới mức đỉnh cao của thể chất, nhờ một thí nghiệm huyết thanh. Evans được phân vai như một phần của hợp đồng đóng cho 3 phim của Marvel. Evans nói rằng nhân vật Steve Rogers sẽ sâu sắc hơn trong The Avengers: "Nó thực sự là việc anh ta cố gắng để đến với Thế giới hiện đại, bạn phải tưởng tượng ra, nó thực sự là một cú sốc để chấp nhận rằng bạn đang ở trong một nơi hoàn toàn khác, những người bạn biết đã không còn, những người bạn quan tâm,.. anh ta là một chiến binh, những người anh ta chiến đấu cùng, tất cả những anh em,.. họ đều đã chết, anh ta hoàn toàn đơn độc. Tôi nghĩ cái phân cảnh bắt đầu, như là việc cá nhảy khỏi nước, nó thực sự khó, như là một viên thuốc đắng mà bạn không dễ dàng gì nuốt nó. Sau đó phải tìm đến sự cân bằng với thế giới hiện tại". Về vấn đề khác nhau giữa Captain và Tony, Evans nói: "Tôi nghĩ đó chắc chắn là một sự phân đôi, sự khác biệt giữa tôi và Tony, một gã thì sặc sỡ, nổi bật và ngọt xớt, một gã thì vị tha, và họ phát hiện rằng mình phải hòa hợp với nhau, trong sự yên lặng. Điều đó khá thú vị đấy".''',
        "Hulk": ''' Một nhà khoa học thiên tài, người mà do sự tiếp xúc với bức xạ gamma đã biến thành một con quái vật khi bị kích thích hoặc tức giận. Ruffalo được phân vai sau thỏa thuận giữa Marvel và Edward Norton thất bại. Về việc thay thế, Ruffalo nói: "Tôi là bạn của Ed, ừ, đó không phải là cách tốt cho chúng tôi. Nhưng cách tôi nhìn nhận vấn đề là Ed đã truyền lại vai diễn này cho tôi". Về nhân vật Hulk, Ruffalo nói: "Anh ta là một người phải đấu tranh với 2 mặt – một sáng một tối, và mọi thứ anh ta làm được thể hiện qua sự kiểm soát của anh ta. Tôi lớn lên trong series truyền hình Bill Bixby TV, nơi mà tôi nghĩ đã cho tôi một sắc thái thực sự và một cách nhìn nhân văn hơn với nhân vật Hulk. Tôi thích những phẩm chất đó". Về vị trí của Hulk trong đội, Ruffalo nói: "Anh ta giống như một đồng đội mà chẳng có ai dám chắc rằng họ muốn có trong đội mình. Anh ấy rất dễ bị kích động. Đây cũng là lần đầu tiên mà diễn viên đóng vai Banner phải đóng luôn vai Hulk". Ruffalo nói với tạp chí New York Times: "Tôi rất hào hứng, chưa ai từng đóng vai Hulk bằng chính mình, họ luôn dùng công nghệ CGI. Còn trong The Avengers, họ sẽ ghi lại những hành động của tôi như phim Avatar vậy, vì thế tôi thực sự đóng vai Hulk, nó thực sự thú vị". Để tạo ra giọng của Hulk, họ dùng giọng của Ruffalo trộn với giọng của Lou Ferrigne và những người khác. Tuy nhiên, câu nói duy nhất của Hulk ("Punny God") được thể hiện duy nhất bằng giọng của Ruffalo.''',
        }
        lookup()
    elif user_input == 2:
        print("Chúc một ngày tốt lành!")
        break
