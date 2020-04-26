import os, time
from tqdm import tqdm

from google_screenshot import GoogleCrawler
from google_screenshot import GoogleScreenCrawler
from yahoo_screenshot import YahooCrawler
from bing_screenshot import BingCrawler
from instagram_screenshot import InstagramCrawler
from mtcnn_face_cropper import mtcnnCropper

out_path = '/media/sf_E/RKB-Dataset/Filipina3/'

daftar_nama = [
    "Aicelle Santos Filipina",
  "Aiko Climaco Filipina",
  "Aiko Melendez Filipina",
  "Aira Bermudez Filipina",
  "Aiza Seguerra Filipina",
  "Agot Isidro Filipina",
  "Aleck Bovick Filipina",
  "Alessandra De Rossi Filipina",
  "Alex Gonzaga Filipina",
  "Alexa Ilacad Filipina",
  "Alice Dixson Filipina",
  "Alicia Alonzo Filipina",
  "Alicia Mayer Filipina",
  "Alicia Vergel Filipina",
  "Alma Bella Filipina",
  "Alma Moreno Filipina",
  "Alodia Gosiengfiao Filipina",
  "Alona Alegre Filipina",
  "Alyssa Alano Filipina",
  "Ama Quiambao Filipina",
  "Amalia Fuentes Filipina",
  "Amy Austria Filipina",
  "Amy Perez Filipina",
  "Ana Capri Filipina",
  "Ana Roces Filipina",
  "Analyn Barro Filipina",
  "Andi Eigenmann Filipina",
  "Andrea Brillantes Filipina",
  "Andrea del Rosario Filipina",
  "Andrea Torres Filipina",
  "Angel Aquino Filipina",
  "Angel Locsin Filipina",
  "Angeli Bayani Filipina",
  "Angeli Gonzales Filipina",
  "Angeli Nicole Sanoy Filipina",
  "Angelica Jones Filipina",
  "Angelica Panganiban Filipina",
  "Angelika Dela Cruz Filipina",
  "Angeline Quinto Filipina",
  "Angelu de Leon Filipina",
  "Anita Linda Filipina",
  "Anja Aguilar Filipina",
  "Ann Li Filipina",
  "Anna Fegi Filipina",
  "Anna Marie Gutierrez Filipina",
  "Anna Larrucea Filipina",
  "Anna Theresa Licaros Filipina",
  "Annabelle Huggins Filipina",
  "Annabelle Rama Filipina",
  "Anne Curtis Filipina",
  "Antoinette Taus Filipina",
  "Ar Angel Aviles Filipina",
  "Ara Mina Filipina",
  "Arci Muñoz Filipina",
  "Ariana Barouk Filipina",
  "Aria Clemente Filipina",
  "Arianne Bautista Filipina",
  "Ariella Arida Filipina",
  "Armida Siguion-Reyna Filipina",
  "Arny Ross Filipina",
  "Arra San Agustin Filipina",
  "Aruray Filipina",
  "Ash Ortega Filipina",
  "Ashley Cabrera Filipina",
  "Asia Agcaoili Filipina",
  "Assunta de Rossi Filipina",
  "Atang dela Rama Filipina",
  "Athena Filipina",
  "Aubrey Miles Filipina",
  "Aurora Sevilla Filipina",
  "Ayanna Oliva Filipina",
  "Ayen Munji-Laurel Filipina",
  "Ayra Mariano Filipina",
  "Bangs Garcia Filipina",
  "Barbara Miguel Filipina",
  "Barbara Perez Filipina",
  "Barbie Almalbis Filipina",
  "Barbie Forteza Filipina",
  "Barbie Imperial Filipina",
  "Bea Alonzo Filipina",
  "Bea Binene Filipina",
  "Bea Nicolas Filipina",
  "Bea Rose Santiago Filipina",
  "Bea Saw Filipina",
  "Beauty Gonzalez Filipina",
  "Bela Padilla Filipina",
  "Bella Flores Filipina",
  "Belle Mariano Filipina",
  "Bettina Carlos Filipina",
  "Beverly Vergel Filipina",
  "Bianca Gonzalez Filipina",
  "Bianca King Filipina",
  "Bianca Manalo Filipina",
  "Bianca Umali Filipina",
  "Bing Loyzaga Filipina",
  "Bituin Escalante Filipina",
  "Boots Anson-Roa Filipina",
  "Brenna Garcia Filipina",
  "Bubbles Paraiso Filipina",
  "Cacai Bautista Filipina",
  "Camille Prats Filipina",
  "Candy Pangilinan Filipina",
  "Caridad Sanchez Filipina",
  "Carina Afable Filipina",
  "Carla Abellana Filipina",
  "Carla Humphries Filipina",
  "Carlene Aguilar Filipina",
  "Carmen Rosales Filipina",
  "Carmencita Abad Filipina",
  "Carmi Martin Filipina",
  "Carmina Villarroel Filipina",
  "Carol Banawa Filipina",
  "Cassandra Ponti Filipina",
  "Celeste Legaspi Filipina",
  "Celia Rodriguez Filipina",
  "Ces Quesada Filipina",
  "Chacha Cañete Filipina",
  "Chanda Romero Filipina",
  "Charee Pineda Filipina",
  "Charice Pempengco Filipina",
  "Charito de Leon Filipina",
  "Charito Solis Filipina",
  "Chariz Solomon Filipina",
  "Charlene Gonzales Filipina",
  "Charo Santos Filipina",
  "Chat Silayan Filipina",
  "Cherie Gil Filipina",
  "Cherry Lou Filipina",
  "Cherry Pie Picache Filipina",
  "Cheska Garcia Filipina",
  "Chichay Filipina",
  "Chin Chin Gutierrez Filipina",
  "Chlaui Malayao Filipina",
  "Chloe Dauden Filipina",
  "Christine Jacob Filipina",
  "Chx Alcala Filipina",
  "Chynna Ortaleza Filipina",
  "Ciara Sotto Filipina",
  "Cielito del Mundo Filipina",
  "Cindy Kurleto Filipina",
  "Claire dela Fuente Filipina",
  "Claudia Zobel Filipina",
  "Claudine Barretto Filipina",
  "Coleen Garcia Filipina",
  "Coleen Perez Filipina",
  "Coney Reyes Filipina",
  "Cris Villonco Filipina",
  "Cristina Aragon Filipina",
  "Cristina Gonzales Filipina",
  "Cristine Reyes Filipina",
  "Cynthia Zamora Filipina",
  "Daiana Menezes Filipina",
  "Daisy Reyes Filipina",
  "Daisy Romualdez Filipina",
  "Danielle Castaño Filipina",
  "Danita Paner Filipina",
  "Daria Ramirez Filipina",
  "Dasuri Choi Filipina",
  "Dawn Zulueta Filipina",
  "Dely Atay-Atayan Filipina",
  "Denise Barbacena Filipina",
  "Denise Joaquin Filipina",
  "Denise Laurel Filipina",
  "Desiree del Valle Filipina",
  "Devon Seron Filipina",
  "Dexter Doria Filipina",
  "Diana Zubiri Filipina",
  "Dianne dela Fuente Filipina",
  "Dianne Medina Filipina",
  "Didith Reyes Filipina",
  "Dimples Cooper Filipina",
  "Dimples Romana Filipina",
  "Dina Bonnevie Filipina",
  "Dionne Monsanto Filipina",
  "Diva Montelaba Filipina",
  "Donita Rose Filipina",
  "Donna Cruz Filipina",
  "Eda Nolan Filipina",
  "Ehra Madrigal Filipina",
  "Elena Balmori Filipina",
  "Elha Nympha Filipina",
  "Elise Estrada Filipina",
  "Elisse Joson Filipina",
  "Eliza Pineda Filipina",
  "Elizabeth Cooper Filipina",
  "Elizabeth Oropesa Filipina",
  "Elizabeth Ramsey Filipina",
  "Ella Cruz Filipina",
  "Ella Guevara Filipina",
  "Elle Ramirez Filipina",
  "Ellen Adarna Filipina",
  "Emma Alegre Filipina",
  "Emma Henry Filipina",
  "Emmanuelle Vera Filipina",
  "Empress Schuck Filipina",
  "Erich Gonzales Filipina",
  "Erika Padilla Filipina",
  "Erlinda Cortes Filipina",
  "Esang de Torres Filipina",
  "Etang Discher Filipina",
  "Ethel Booba Filipina",
  "Eugene Domingo Filipina",
  "Eula Caballero Filipina",
  "Eula Valdez Filipina",
  "Eunice Lagusad Filipina",
  "Eva Castillo Filipina",
  "Eva Darren Filipina",
  "Eva Eugenio Filipina",
  "Evangeline Pascual Filipina",
  "Fe Amorsolo Filipina",
  "Fely Acuna Filipina",
  "Frances Makil-Ignacio Filipina",
  "Francine Diaz Filipina",
  "Francine Prieto Filipina",
  "Frencheska Farr Filipina",
  "Franchesca Salcedo Filipina",
  "Fretzie Joan Bercede Filipina",
  "G. Toengi Filipina",
  "Gabbi Garcia Filipina",
  "Gaby dela Merced Filipina",
  "Gee-Ann Abrahan Filipina",
  "Gelli de Belen Filipina",
  "Gem Ramos Filipina",
  "Geneva Cruz Filipina",
  "Georgina Wilson Filipina",
  "Geraldine Villarruz Asis Filipina",
  "Gina Alajar Filipina",
  "Gina Pareño Filipina",
  "Gladys Guevarra Filipina",
  "Gladys Reyes Filipina",
  "Glaiza de Castro Filipina",
  "Gloria Diaz Filipina",
  "Gloria Romero Filipina",
  "Gloria Sevilla Filipina",
  "Glydel Mercado Filipina",
  "Grace Lee Filipina",
  "Gretchen Espina Filipina",
  "Gretchen Barretto Filipina",
  "Gwen Garci Filipina",
  "Gwen Zamora Filipina",
  "Halina Perez Filipina",
  "Harlene Bautista Filipina",
  "Hazel Ann Mendoza Filipina",
  "Heart Evangelista Filipina",
  "Helen Gamboa Filipina",
  "Helen Vela Filipina",
  "Helga Krapf Filipina",
  "Hilda Koronel Filipina",
  "Hiyasmin Neri Filipina",
  "Ian Galliguez Filipina",
  "Imelda Papin Filipina",
  "Imelda Schweighart Filipina",
  "Ina Feleo Filipina",
  "Ina Raymundo Filipina",
  "Inday Badiday Filipina",
  "Ingrid dela Paz Filipina",
  "Irma Adlawan Filipina",
  "Isabel Blaesi Filipina",
  "Isabel Granada Filipina",
  "Isabel Oli Filipina",
  "Isabella de Leon Filipina",
  "Isabelle Daza Filipina",
  "Iwa Moto Filipina",
  "Iya Villania Filipina",
  "Iza Calzado Filipina",
  "Jackie Lou Blanco Filipina",
  "Jackie Rice Filipina",
  "Jaclyn Jose Filipina",
  "Jade Ecleo Filipina",
  "Jade Lopez Filipina",
  "Jan Marini Filipina",
  "Jana Roxas Filipina",
  "Jane Oineza Filipina",
  "Janella Salvador Filipina",
  "Janelle Jamer Filipina",
  "Janelle Quintana Filipina",
  "Janice de Belen Filipina",
  "Janina San Miguel Filipina",
  "Janine Gutierrez Filipina",
  "Janine Tugonon Filipina",
  "Janna Dominguez Filipina",
  "January Isaac Filipina",
  "Jasmine Curtis-Smith Filipina",
  "Jaya Ramsey Filipina",
  "Jaymee Joaquin Filipina",
  "Jazz Ocampo Filipina",
  "Jean Garcia Filipina",
  "Jed Montero Filipina",
  "Jef Gaitan Filipina",
  "Jennica Garcia Filipina",
  "Jennifer Sevilla Filipina",
  "Jenny Miller Filipina",
  "Jennylyn Mercado Filipina",
  "Jessa Zaragoza Filipina",
  "Jessy Mendiola Filipina",
  "Jewel Mische Filipina",
  "Jhoana Marie Tan Filipina",
  "Jillian Ward Filipina",
  "Jinri Park Filipina",
  "Joanne Quintas Filipina",
  "Jocelyn Oxlade Filipina",
  "Jodi Santamaria Filipina",
  "Jolina Magdangal Filipina",
  "Jonalyn Viray Filipina",
  "Jopay Paguia Filipina",
  "Joyce Ching Filipina",
  "Joyce Jimenez Filipina",
  "Joy Viado Filipina",
  "Juanita Angeles Filipina",
  "Judy Ann Santos Filipina",
  "Julia Barretto Filipina",
  "Julia Clarete Filipina",
  "Julia Montes Filipina",
  "Julie Anne San Jose Filipina",
  "Julie Vega Filipina",
  "Justina David Filipina",
  "Juvy Cachola Filipina",
  "K Brosas Filipina",
  "Karel Marquez Filipina",
  "Karen delos Reyes Filipina",
  "Karen Reyes Filipina",
  "Karla Estrada Filipina",
  "Karylle Filipina",
  "Kat Alano Filipina",
  "Kate Valdez Filipina",
  "Kathleen Hermosa Filipina",
  "Kathryn Bernardo Filipina",
  "Katrina Halili Filipina",
  "Katy de la Cruz Filipina",
  "Katya Santos Filipina",
  "Kaye Abad Filipina",
  "KC Concepcion Filipina",
  "Keanna Reeves Filipina",
  "Kim Chiu Filipina",
  "Kim Domingo Filipina",
  "Kim Molina Filipina",
  "Kim Rodriguez Filipina",
  "Kiray Filipina",
  "Kisses Delavin Filipina",
  "Kitchie Nadal Filipina",
  "Kitkat Filipina",
  "Klaudia Koronel Filipina",
  "Koreen Medina Filipina",
  "Kris Aquino Filipina",
  "Kris Bernal Filipina",
  "Krista K Filipina",
  "Krista Ranillo Filipina",
  "Kristel Fulgar Filipina",
  "Kristel Moreno Filipina",
  "Kristina Paner Filipina",
  "Kristine Hermosa Filipina",
  "Krizza Neri Filipina",
  "Krystal Reyes Filipina",
  "Kuh Ledesma Filipina",
  "Kyla Filipina",
  "Kylie Padilla Filipina",
  "Kylie Verzosa Filipina",
  "Kyline Alcantara Filipina",
  "KZ Tandingan Filipina",
  "Lady Lee Filipina",
  "Lana Jalosjos Filipina",
  "Lani Mercado Filipina",
  "Lani Misalucha Filipina",
  "Lauren Young Filipina",
  "Laurice Guillen Filipina",
  "Lea Salonga Filipina",
  "Leanne Bautista Filipina",
  "Letty Alonzo Filipina",
  "Lexi Fernandez Filipina",
  "Liezel Lopez Filipina",
  "Lilet Filipina",
  "Lilia Cuntapay Filipina",
  "Lilia Dizon Filipina",
  "Lilian Velez Filipina",
  "Linda Estrella Filipina",
  "Linn Oeymo Filipina",
  "Liz Alindogan Filipina",
  "Liza Diño Filipina",
  "Liza Lorena Filipina",
  "Liza Soberano Filipina",
  "LJ Reyes Filipina",
  "Loisa Andalio Filipina",
  "Lolit Solis Filipina",
  "Lolita Rodriguez Filipina",
  "Lorna Tolentino Filipina",
  "Lota Delgado Filipina",
  "Lotlot de Leon Filipina",
  "Lougee Basabas Filipina",
  "Louise delos Reyes Filipina",
  "Lovely Abella Filipina",
  "Lovely Rivero Filipina",
  "Lovi Poe Filipina",
  "Luane Dy Filipina",
  "Lucita Soriano Filipina",
  "Lucy Torres Filipina",
  "Luz Valdez Filipina",
  "Lyca Gairanod Filipina",
  "Maey Bautista Filipina",
  "Maika Rivera Filipina",
  "Maine Mendoza Filipina",
  "Maja Salvador Filipina",
  "Malou de Guzman Filipina",
  "Manilyn Reynes Filipina",
  "Mara Lopez Filipina",
  "Margaret Nales Wilson Filipina",
  "Maria Amapola Cabase Filipina",
  "Maria Isabel Lopez Filipina",
  "Maria Teresa Carlson Filipina",
  "Marian Rivera Filipina",
  "Marianne dela Riva Filipina",
  "Maricar de Mesa Filipina",
  "Maricar Reyes Filipina",
  "Maricel Laxa Filipina",
  "Maricel Soriano Filipina",
  "Maricris Garcia Filipina",
  "Mariel Pamintuan Filipina",
  "Mariel Rodriguez Filipina",
  "Marife Necesito Filipina",
  "Maris Racal Filipina",
  "Marissa Delgado Filipina",
  "Marita Zobel Filipina",
  "Maritoni Fernandez Filipina",
  "Mariz Ricketts Filipina",
  "Marjorie Barretto Filipina",
  "Marla Boyd Filipina",
  "Marlann Flores Filipina",
  "Marlene Dauden Filipina",
  "Marvelous Alejo Filipina",
  "Mary Walter Filipina",
  "Mary Jean Lastimosa Filipina",
  "Matet de Leon Filipina",
  "Matimtiman Cruz Filipina",
  "Maui Taylor Filipina",
  "Maureen Francisco Filipina",
  "Maureen Larrazabal Filipina",
  "Maureen Mauricio Filipina",
  "Max Collins Filipina",
  "Maxine Medina Filipina",
  "Maxene Magalona Filipina",
  "Maybelyn dela Cruz Filipina",
  "Maymay Entrata Filipina",
  "Mayton Eugenio Filipina",
  "Meg Imperial Filipina",
  "Megan Young Filipina",
  "Melai Cantiveros Filipina",
  "Melanie Marquez Filipina",
  "Melissa Mendez Filipina",
  "Melissa Ricks Filipina",
  "Mely Tagasa Filipina",
  "Mercedes Cabral Filipina",
  "Metring David Filipina",
  "Mich Dulce Filipina",
  "Michelle Madrigal Filipina",
  "Michelle van Eimeren Filipina",
  "Mickey Ferriols Filipina",
  "Miho Nishida Filipina",
  "Mika Dela Cruz Filipina",
  "Mikee Cojuangco-Jaworski Filipina",
  "Mikee Quintos Filipina",
  "Mila del Sol Filipina",
  "Miles Ocampo Filipina",
  "Miriam Quiambao Filipina",
  "Mona Lisa Filipina",
  "Mona Louise Rey Filipina",
  "Morissette Amon Filipina",
  "Mosang Filipina",
  "Mutya Datul Filipina",
  "Mutya Orquia Filipina",
  "Mylene Dizon Filipina",
  "Myrtle Sarrosa Filipina",
  "Nadine Lustre Filipina",
  "Nadine Samonte Filipina",
  "Nancy Castiglione Filipina",
  "Nanette Medved Filipina",
  "Nathalie Hart Filipina",
  "Naty Bernardo Filipina",
  "Nela Alvarez Filipina",
  "Nena Cardenas Filipina",
  "Nene Tamayo Filipina",
  "Neri Naig Filipina",
  "Nicole Dulalia Filipina",
  "Nicole Uysiuseng Filipina",
  "Nida Blanca Filipina",
  "Nikka Valencia Filipina",
  "Nikki Bacolod Filipina",
  "Nikki Gil Filipina",
  "Nikki Valdez Filipina",
  "Nina Girado Filipina",
  "Nina Kodaka Filipina",
  "Niña Dolino Filipina",
  "Niña Jose Filipina",
  "Nora Aunor Filipina",
  "Nori Dalisay Filipina",
  "Nova Villa Filipina",
  "Olivia Cenizal Filipina",
  "Pacita del Rio Filipina",
  "Paraluman Filipina",
  "Patricia Fernandez Filipina",
  "Patricia Tumulak Filipina",
  "Paula Peralejo Filipina",
  "Pauleen Luna Filipina",
  "Pauline Mendoza Filipina",
  "Paw Diaz Filipina",
  "Perla Bautista Filipina",
  "Phoemela Barranda Filipina",
  "Pia Guanio Filipina",
  "Pia Moran Filipina",
  "Pia Wurtzbach Filipina",
  "Pilar Pilapil Filipina",
  "Pilita Corrales Filipina",
  "Pinky Amador Filipina",
  "Pokwang Filipina",
  "Pops Fernandez Filipina",
  "Precious Lara Quigaman Filipina",
  "Princess Guevarra Filipina",
  "Princess Punzalan Filipina",
  "Princess Ryan Filipina",
  "Puentespina Riza Filipina",
  "Queneerich Rehman Filipina",
  "Rachel Alejandro Filipina",
  "Rachelle Ann Go Filipina",
  "Radha Cuadrado Filipina",
  "Raquel Monteza Filipina",
  "Raven Villanueva Filipina",
  "Rebecca del Rio Filipina",
  "Rebecca Lusterio Filipina",
  "Regine Angeles Filipina",
  "Regine Tolentino Filipina",
  "Regine Velasquez Filipina",
  "Rhian Ramos Filipina",
  "Ria Atayde Filipina",
  "Rica Peralejo Filipina",
  "Rich Asuncion Filipina",
  "Rio Diaz Filipina",
  "Rio Locsin Filipina",
  "Rita Amor Filipina",
  "Rita Avila Filipina",
  "Rita Iringan Filipina",
  "Rita Rio Filipina",
  "Ritz Azul Filipina",
  "Riza Santos Filipina",
  "Rochelle Pangilinan Filipina",
  "Rosa Aguirre Filipina",
  "Rosa del Rosario Filipina",
  "Rosa Mia Filipina",
  "Rosa Rosal Filipina",
  "Rosanna Roces Filipina",
  "Roselle Nava Filipina",
  "Rosemarie Gil Filipina",
  "Rosita Capuyon Filipina",
  "Rosemarie Sonora Filipina",
  "Rox Montealegre Filipina",
  "Roxanne Barcelo Filipina",
  "Roxanne Guinoo Filipina",
  "RR Enriquez Filipina",
  "Ruby Moreno Filipina",
  "Ruby Rodriguez Filipina",
  "Rufa Mae Quinto Filipina",
  "Rufa Mi Filipina",
  "Ruffa Gutierrez Filipina",
  "Ryza Cenon Filipina",
  "Ryzza Mae Dizon Filipina",
  "Saab Magalona Filipina",
  "Sabrina Man Filipina",
  "Sam Bumatay Filipina",
  "Sam Pinto Filipina",
  "Sandara Park Filipina",
  "Sandy Andolong Filipina",
  "Sandy Talag Filipina",
  "Sanya Lopez Filipina",
  "Sarah Geronimo Filipina",
  "Sarah Lahbati Filipina",
  "Say Alonzo Filipina",
  "Scarlet Garcia Filipina",
  "Serena Dalrymple Filipina",
  "Shaina Magdayao Filipina",
  "Shaira Diaz Filipina",
  "Shamaine Buencamino Filipina",
  "Shamcey Supsup Filipina",
  "Sharlene San Pedro Filipina",
  "Sharmaine Arnaiz Filipina",
  "Sharon Cuneta Filipina",
  "Sheena Halili Filipina",
  "Sheree Bautista Filipina",
  "Sherilyn Reyes-Tan Filipina",
  "Shermaine Santiago Filipina",
  "Sheryl Cruz Filipina",
  "Sheryn Regis Filipina",
  "Shey Bustamante Filipina",
  "Shine Kuk Filipina",
  "Shy Carlos Filipina",
  "Snooky Serna Filipina",
  "Sofie Garrucho Filipina",
  "Solenn Heussaff Filipina",
  "Sofia Andres Filipina",
  "Sophia Montecarlo Filipina",
  "Sophie Albert Filipina",
  "Stef Prescott Filipina",
  "Stephanie Sol Filipina",
  "Sue Prado Filipina",
  "Sue Ramirez Filipina",
  "Sugar Mercado Filipina",
  "Sunshine Cruz Filipina",
  "Sunshine Dizon Filipina",
  "Susan Africa Filipina",
  "Susan Roces Filipina",
  "Suzette Ranillo Filipina",
  "Sylvia La Torre Filipina",
  "Sylvia Sanchez Filipina",
  "Taki Saito Filipina",
  "Tanya Garcia Filipina",
  "Tessie Agana Filipina",
  "Tessie Tomas Filipina",
  "Tetchie Agbayani Filipina",
  "Thea Tolentino Filipina",
  "Therese Malvar Filipina",
  "Dee ira A Fortes Filipina",
  "Tippy Dos Santos Filipina",
  "Tita de Villa Filipina",
  "Tita Duran Filipina",
  "Tita Muñoz Filipina",
  "Toni Gonzaga Filipina",
  "Toni Rose Gayda Filipina",
  "Tootsie Guevara Filipina",
  "Tuesday Vargas Filipina",
  "Valeen Montenegro Filipina",
  "Valerie Concepcion Filipina",
  "Valerie Weigmann Filipina",
  "Vaness del Moral Filipina",
  "Venus Raj Filipina",
  "Verna Gaston Filipina",
  "Vicki Belo Filipina",
  "Vickie Rushton Filipina",
  "Vilma Santos Filipina",
  "Vina Morales Filipina",
  "Vivian Velez Filipina",
  "Wendy Valdez Filipina",
  "Wynwyn Marquez Filipina",
  "Xia Vigor Filipina",
  "Xyriel Manabat Filipina",
  "Yam Concepcion Filipina",
  "Yasmien Kurdi Filipina",
  "Yassi Pressman Filipina",
  "Yayo Aguila Filipina",
  "Yen Santos Filipina",
  "Yeng Constantino Filipina",
  "Yesha Camile Filipina",
  "Ylona Garcia Filipina",
  "Ynna Asistio Filipina",
  "Zandra Summer Filipina",
  "Zeny Zabala Filipina",
  "Zeryl Lim Filipina",
  "Zia Marquez Filipina",
  "Zia Quizon Filipina",
  "Zorayda Sanchez Filipina",
  "Zsa Zsa Padilla Filipina"
]

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def cropper():
	print("cropping for", nama)
	nama_path = os.path.join(out_path,nama)
	filenames = files(nama_path)
	for filename in filenames:
		mtcnnCropper(nama_path, filename)

for index, nama in enumerate(daftar_nama):
	try:
		GoogleCrawler(nama, out_path)
		# GoogleScreenCrawler(nama, out_path)
		# YahooCrawler(nama, out_path)
		# BingCrawler(nama, out_path)
		# InstagramCrawler(nama, out_path)
		
		# cropper()

	# 	if index < (len(daftar_nama) - 1):
	# 		for i in tqdm(range(50)):
	# 			time.sleep(1)
	except:
		print("failed or incomplete operation on", nama)