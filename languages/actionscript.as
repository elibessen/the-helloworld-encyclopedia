import flash.text.TextField;
import flash.text.TextFormat;

var message:TextField = new TextField();
message.x = message.y = 5;
message.width = 300;
message.height = 50;

var tf:TextFormat = new TextFormat(); 
tf.color = 0xFF0000;
tf.size = 32;
tf.bold = true;

message.defaultTextFormat = tf;
message.text = "Hello World!";
MovieClip(root).addChild(message);