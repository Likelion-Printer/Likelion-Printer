let container = document.getElementById('map_box'); //지도를 담을 영역의 DOM 레퍼런스
let options = { //지도를 생성할 때 필요한 기본 옵션
	center: new kakao.maps.LatLng(37.5968599, 127.0596229), //지도의 중심좌표.
	level: 3 //지도의 레벨(확대, 축소 정도)
};

let map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

class printPlace {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

let place = new printPlace(37.596324, 127.060255);
let place2 = new printPlace(37.596626, 127.060540);
let place3 = new printPlace(37.595989, 127.060073);


// 마커가 표시될 위치입니다 
let markerPosition  = new kakao.maps.LatLng(place.x, place.y); 
// 마커를 생성합니다
let marker1 = new kakao.maps.Marker({
    position: markerPosition
});
marker1.setMap(map);


markerPosition  = new kakao.maps.LatLng(place2.x, place2.y); 
let marker2 = new kakao.maps.Marker({
    position: markerPosition
});
marker2.setMap(map);


markerPosition  = new kakao.maps.LatLng(place3.x, place3.y); 
let marker3 = new kakao.maps.Marker({
    position: markerPosition
});
marker3.setMap(map);

// 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// marker.setMap(null);    

// 마커를 클릭했을 때 마커 위에 표시할 인포윈도우를 생성합니다
let iwContent = '<div style="width:120px; height:33px; background-color:#7558EE;">B 문우인쇄소</div>'; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다

// 인포윈도우를 생성합니다
let infowindow = new kakao.maps.InfoWindow({
    content : iwContent,
    removable : false
});


let t = document.getElementById('h');

t.addEventListener('click', function(event){
    infowindow.open(map, marker1);  
});
