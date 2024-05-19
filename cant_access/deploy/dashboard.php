<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LFI Lab</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #ffe6e6; /* Pink background */
            color: #4a4a4a; /* Dark grey text */
        }

        .card-header {
            background-color: #ffcccb; /* Light pink */
            color: #4a4a4a; /* Dark grey text */
        }

        .card-body {
            background-color: #fff3cd; /* Light yellow */
            color: #4a4a4a; /* Dark grey text */
        }

        .container {
            margin-top: 5rem;
        }

        .card {
            border: 1px solid #ffcccb; /* Light pink border */
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card">
                    <div class="card-header">
                        DATA
                    </div>
                    <div class="card-body">
                        <?php
                        require ("db.php");
                        if ($_SERVER['REQUEST_METHOD'] == 'GET') {
                            try {
                                $title = $_GET['title'];
                                $sql = "SELECT * FROM upload WHERE title LIKE '$title'";
                                $result = $conn->query($sql);
                                if ($row = $result->fetch_assoc()) {
                                    echo '<h5 class="card-title">' . htmlspecialchars($row['title']) . '</h5>';
                                    echo '<img src="/uploads/' . htmlspecialchars($row['filename']) . '" alt="Image" class="img-fluid mb-3">';
                                    echo '<p class="card-text">' . htmlspecialchars($row['content']) . '</p>';
                                } else {
                                    echo "<p>No records found.</p>";
                                }
                            } catch (mysqli_sql_exception $e) {
                                echo "<p>Query failed: " . $e->getMessage() . "</p>";
                            }
                        } else {
                            echo "<script>alert('Only GET requests are allowed');</script>";
                            echo "<script>window.location.href = '/index.php';</script>";
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>

</html>
