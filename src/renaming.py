from datetime import datetime
import config as config


# Readable month formats
RMs = {12: "Dec", 11: "Nov", 10: "Oct", 9: "Sept", 8: "Aug", 7: "July", 1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May",  6: "June"}
RMMs = { 12: "December", 11: "November", 10: "Octobre", 9: "September", 8: "August", 7: "July", 1: "January", 2: "Febuary", 3: "March", 4: "April", 5: "May",  6: "June" }



def RENAME(filename, new_filename):
    # "2019051913454200-F1C11A22FAEE3B82F21B330E1B786A39"
    date = datetime(
        year=int(filename[0:4]),
        month=int(filename[4:6]),
        day=int(filename[6:8]),
        hour=int(filename[8:10]),
        minute=int(filename[10:12]),
        second=int(filename[12:14])
    )


    DATE_VARIABLES = {
        "YYYY": date.year,
        "MM": date.month,
        "DD": date.day,
        "4hh": date.hour,   # 24 hour time
        "mm": date.minute,
        "ss": date.second,
        "2hh": date.hour if date.hour <= 12 else date.hour - 12,  # 12 hour time

        "RM": RMs[date.month],  # Readable month
        "RMM": RMMs[date.month]  # Long readable month
    }
    return new_filename.format(**DATE_VARIABLES)


if "__main__" == __name__:
    RENAME("2019051913454200-F1C11A22FAEE3B82F21B330E1B786A39", config.FILENAME_FORMAT)