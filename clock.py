import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
public class TimeImageGenerator {
    public static void main(String[] args) {
        try {
            BufferedImage image = new BufferedImage(100, 20, BufferedImage.TYPE_INT_RGB);
            Graphics2D g2d = image.createGraphics();
            g2d.setColor(Color.BLACK);
            g2d.fillRect(0, 0, 100, 20);
            g2d.setFont(new Font("Arial", Font.BOLD, 16));
            g2d.setColor(Color.WHITE);
            g2d.drawString("08:17 AM", 10, 15);
            g2d.dispose();
            ImageIO.write(image, "png", new File("time.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
