
        $(document).ready(function() {
                $("#input_file").bind('change', function() {
                    selectFile(this.files);
                    //this.files[0].size gets the size of your file.
                    //alert(this.files[0].size);
                });
            });
        
            // 파일 리스트 번호
            let fileIndex = 0;
            // 등록할 전체 파일 사이즈
            let totalFileSize = 0;
            // 파일 리스트
            let fileList = new Array();
            // 파일 사이즈 리스트
            let fileSizeList = new Array();
            // 등록 가능한 파일 사이즈 MB
            let uploadSize = 50;
            // 등록 가능한 총 파일 사이즈 MB
            let maxUploadSize = 500;
    
            $(function() {
                // 파일 드롭 다운
                fileDropDown();
            });
    
            // 파일 드롭 다운
            function fileDropDown() {
                let dropZone = $("#dropZone");
                //Drag기능 
                dropZone.on('dragenter', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                    // 드롭다운 영역 css
                    dropZone.css('background-color', '#D4D2E6');
                });
                dropZone.on('dragleave', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                    // 드롭다운 영역 css
                    dropZone.css('background-color', '#FAFAFA');
                });
                dropZone.on('dragover', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                    // 드롭다운 영역 css
                    dropZone.css('background-color', '#D4D2E6');
                });
                dropZone.on('drop', function(e) {
                    e.preventDefault();
                    // 드롭다운 영역 css
                    dropZone.css('background-color', '#FAFAFA');
                    // 하나씩 찍힘
                    let files = e.originalEvent.dataTransfer.files;
                    // console.log(files);
                    if (files != null) {
                        if (files.length < 1) {
                            /* alert("폴더 업로드 불가"); */
                            console.log("파일 업로드 불가");
                            return;
                        } else {
                            selectFile(files)
                        }
                    } else {
                        alert("ERROR");
                    }
                });
            }
    
            // 파일 선택시
            function selectFile(fileObject) {
                let files = null;
    
                if (fileObject != null) {
                    // 파일 Drag 이용하여 등록시
                    files = fileObject;
                    // console.log(files)
                } else {
                    // 직접 파일 등록시
                    files = $('#multipaartFileList_' + fileIndex)[0].files;
                }
    
                // 다중파일 등록
                if (files != null) {
                    
                    if (files != null && files.length > 0) {
                        $("fileListTable").show();
                        $("#fileDragDesc").show();
                    } else {
                        $("#fileDragDesc").show(); 
                        $("fileListTable").hide();
                    }addFileList            
                    
                    for (let i = 0; i < files.length; i++) {
                        // 파일 이름
                        let fileName = files[i].name;
                        // console.log(files[i].name)
                        let fileNameArr = fileName.split("\.");
                        // 확장자
                        let ext = fileNameArr[fileNameArr.length - 1];
                        
                        let fileSize = files[i].size; // 파일 사이즈(단위 :byte)
                        console.log("fileSize="+fileSize);
                        if (fileSize <= 0) {
                            console.log("0kb file return");
                            return;
                        }
                        
                        let fileSizeKb = fileSize / 1024; // 파일 사이즈(단위 :kb)
                        let fileSizeMb = fileSizeKb / 1024;    // 파일 사이즈(단위 :Mb)
                        
                        let fileSizeStr = "";
                        if ((1024*1024) <= fileSize) {    // 파일 용량이 1메가 이상인 경우 
                            console.log("fileSizeMb="+fileSizeMb.toFixed(2));
                            fileSizeStr = fileSizeMb.toFixed(2) + " Mb";
                        } else if ((1024) <= fileSize) {
                            console.log("fileSizeKb="+parseInt(fileSizeKb));
                            fileSizeStr = parseInt(fileSizeKb) + " kb";
                        } else {
                            console.log("fileSize="+parseInt(fileSize));
                            fileSizeStr = parseInt(fileSize) + " byte";
                        }
    
                        /* if ($.inArray(ext, [ 'exe', 'bat', 'sh', 'java', 'jsp', 'html', 'js', 'css', 'xml' ]) >= 0) {
                            // 확장자 체크
                            alert("등록 불가 확장자");
                            break; */
                        if ($.inArray(ext, [ 'hwp', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'png', 'pdf', 'jpg', 'jpeg', 'gif', 'zip' ]) <= 0) {
                            // 확장자 체크
                            /* alert("해당 파일은 업로드할 수 없어요(｡･ˇ_ˇ･｡).");
                            break; */
                            alert("해당 파일은 업로드할 수 없어욧..⁺◟( ᵒ̴̶̷̥́ ·̫ ᵒ̴̶̷̣̥̀ )..("+fileName+")");
                        } else if (fileSizeMb > uploadSize) {
                            // 파일 사이즈 체크
                            alert("용량 초과\n업로드 가능 용량 : " + uploadSize + " MB");
                            break;
                        } else {
                            // 전체 파일 사이즈
                            totalFileSize += fileSizeMb;
    
                            // console.log(fileList);
                            // 파일 배열에 넣기
                            fileList[fileIndex] = files[i];
    
                            // 파일 사이즈 배열에 넣기
                            fileSizeList[fileIndex] = fileSizeMb;
    
                            // 업로드 파일 목록 생성
                            addFileList(fileIndex, fileName, fileSizeStr);
    
                            // 파일 번호 증가
                            fileIndex++;
                        }
                    }
                } else {
                    alert("ERROR");
                }
            }
    
            // 업로드 파일 목록 생성
            function addFileList(fIndex, fileName, fileSizeStr) {
                /* if (fileSize.match("^0")) {
                    alert("start 0");
                } */
    
                let html = "";
                html += "<tr id='fileTr_" + fIndex + "'>";
                html += "    <td id='dropZone_' class='left' >";
                html += fileName + " (" + fileSizeStr +") " 
                        //+ "<a href='#' onclick='deleteFile(" + fIndex + "); return false;' class='btn small bg_02'> 삭제</a>"
                        
                        + "<button id='delete_button' value='삭제' href='#' onclick='deleteFile(" + fIndex + "); return false;'></button>"
                html += "    </td>"
                html += "</tr>"
    
                $('#fileTableTbody').append(html);
            }
    
            // 업로드 파일 삭제
            function deleteFile(fIndex) {
                console.log("deleteFile.fIndex=" + fIndex);
                // 전체 파일 사이즈 수정
                totalFileSize -= fileSizeList[fIndex];
    
                // 파일 배열에서 삭제
                delete fileList[fIndex];
    
                // 파일 사이즈 배열 삭제
                delete fileSizeList[fIndex];
    
                // 업로드 파일 테이블 목록에서 삭제
                $("#fileTr_" + fIndex).remove();
                
                console.log("totalFileSize="+totalFileSize);
                
                if (totalFileSize > 0) {
                    $("#fileDragDesc").show(); 
                    $("fileListTable").show();
                } else {
                    $("#fileDragDesc").show(); 
                    $("fileListTable").hide();
                }
            }
    
            // 파일 등록
            function uploadFile() {
                // 등록할 파일 리스트
                let uploadFileList = Object.keys(fileList);
    
                // 파일이 있는지 체크
                if (uploadFileList.length == 0) {
                    // 파일등록 경고창
                    alert("파일이 없습니다.");
                    return;
                }
    
                // 용량을 500MB를 넘을 경우 업로드 불가
                if (totalFileSize > maxUploadSize) {
                    // 파일 사이즈 초과 경고창
                    alert("총 용량 초과\n총 업로드 가능 용량 : " + maxUploadSize + " MB");
                    return;
                }
    
                if (confirm("등록 하시겠습니까?")) {
                    // 등록할 파일 리스트를 formData로 데이터 입력
                    let form = $('#uploadForm');
                    let formData = new FormData();
                    // console.log(files)
                    // 하나만 보내게 수정
                    console.log(fileList[uploadFileList[0]]);
                    formData.append('file', fileList[uploadFileList[0]]);
                    
                    $.ajax({
                        url : "http://127.0.0.1:8000/orders/file_api",
                        data : formData,
                        type : 'POST',
                        enctype : 'multipart/form-data',
                        processData : false,
                        contentType : false,
                        dataType : 'json',
                        cache : false,
                        success : function(result) {
                            if (result.data.length > 0) {
                                alert("성공");
                                location.reload();
                            } else {
                                alert("실패");
                                location.reload();
                            }
                        }
                    });
                }
            }
   