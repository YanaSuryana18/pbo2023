CREATE TABLE obat (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255) UNIQUE,
    jenis ENUM('Obat Cair','Tablet','Kapsul','Obat Oles','Obat Tetes'),
    harga INT,
    stok INT,
    UNIQUE(nama)
);

CREATE TABLE pembeli (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255) UNIQUE,
    alamat VARCHAR(255),
    jenis_kelamin ENUM('Laki laki', 'Perempuan'),
    UNIQUE(nama)
);

CREATE TABLE penjualan (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_obat INT,
    id_pembeli INT,
    total_obat INT,
    harga INT,
    total_harga INT,
    waktu DATE,
    FOREIGN KEY (id_obat) REFERENCES obat(id),
    FOREIGN KEY (id_pembeli) REFERENCES pembeli(id),
    UNIQUE(id_obat, id_pembeli)
);
