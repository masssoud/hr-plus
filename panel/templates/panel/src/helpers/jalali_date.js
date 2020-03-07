import moment from 'jalali-moment';

class JalaliDateHelper {
    static gregorianToJalali = (gregorian, jalaliFormat) => {
        const date = moment(gregorian);
        return date.locale('fa').format(jalaliFormat);
    }
}

export default JalaliDateHelper;