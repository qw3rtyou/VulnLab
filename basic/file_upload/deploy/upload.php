<?php
require ("db.php");
if ($_SERVER['REQUEST_METHOD'] == 'POST' and $_POST['title'] and $_POST['content']) {
    if (isset($_FILES['file']) && $_FILES['file']['error'] == 0) {
        $uploadPath = './uploads/';
        $fileExtension = pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);
        $fileName = uniqid("file_", true) . '.' . $fileExtension;

        if (!is_dir($uploadPath)) {
            mkdir($uploadPath, 0777, true);
        }
        if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadPath . $fileName)) {
            try {
                $title = $_POST['title'];
                $content = $_POST['content'];
                $stmt = $conn->prepare("INSERT INTO upload (title, content,filename) VALUES (?, ?, ?)");
                $stmt->bind_param('sss', $title, $content, $fileName);

                $stmt->execute();
            } catch (mysqli_sql_exception $e) {
                echo "Query failed: " . $e->getMessage();
            }
            echo "<script>alert('$fileName')</script>";
            echo "<script>location.href='/dashboard.php?title=$title'</script>";
        } else {
            echo "<script>alert('Something wrong..');</script>";
            echo "<script>location.href='/index.php'</script>";
        }
    }

} else {
    ?>
    <!DOCTYPE html>
    <html>

    <head>
        <title>Upload File</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>

    <body class="bg-dark text-white">
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-6 offset-md-3">
                    <div class="card card-body bg-secondary">
                        <h2 class="text-center">Upload</h2>
                        <form action="/upload.php" method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <label for="title">Title</label>
                                <input type="text" id="title" name="title" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="content">Details</label>
                                <textarea id="content" name="content" rows="4" class="form-control"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="file">Attach Image</label>
                                <input type="file" id="file" name="file" class="form-control-file">
                            </div>
                            <div class="form-group">
                                <input type="submit" value="Upload" class="btn btn-primary">
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>

    </html>
    <?php

}
?>